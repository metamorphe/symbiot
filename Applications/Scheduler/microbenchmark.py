# Runs microbenchmark tests

import Queue, math, json
import expresso_api as api
from job import Job
from pprint import pprint
import jnd_arduino as jnd
import scheduler as scheduler

directory = "microbenchmarks/"
benchmark_file = 'tests.yaml'

def preprocess(): 
	files = [line.strip() for line in open(directory + benchmark_file, 'r') if line[0] != "#" and len(line) > 1]
	
	tests = []
	for f in files:
		data = get_json(directory + f)
		commands = []
		for d in data: 
			commands.append((d["addr"], d["flavor_id"], d["behavior_id"], d["t0"]))
		tests.append((f, microbenchmark(commands, 1)))
	return tests

def get_json(filename):
	json_data = open(filename)
	data = json.load(json_data)
	json_data.close()
	return data

def microbenchmark(commands, velocity=1):
	q = Queue.PriorityQueue(maxsize=0)
	for addr, f_id, b_id, t0 in commands:
		for t, v in api.get_commands(b_id, velocity):
			if math.isnan(v):
				q.put(Job(b_id, f_id, t + t0, 0, addr))
			else:
				q.put(Job(b_id, f_id, t + t0, v, addr))
	compiled_commands = []
	while not q.empty():
		compiled_commands.append(q.get())
	return compiled_commands


def calc_collisions(commands):
	collisions = {}
	size = len(commands)

	for c in commands: 
		try:
			collisions[c.priority].append(c)
		except KeyError, e:
			collisions[c.priority] = []

	# count collisions
	conflicts = dict([(timestamp, len(jobs)) for timestamp, jobs in collisions.iteritems() if len(jobs) > 2])
	# sum of collisions
	sum = 0.
	for t, c in conflicts.iteritems():
		sum += c

	return sum/size

def run(tests):
	master = jnd.JNDArduino();
	master.open()
	for name, commands in tests:
		print name
		print "COLLISION RATE: ", calc_collisions(commands), "N:", len(commands)
		scheduler.send(master, commands)
	master.close()

def main(): 
	tests = preprocess()
	run(tests)
if __name__ == "__main__": ard = main()


