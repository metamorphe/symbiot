# Runs microbenchmark tests

import Queue, math, json, sys
sys.path.append('lib')
from job import Job
from pprint import pprint
import jnd_arduino as jnd
import scheduler as scheduler
import  time, yaml
from microtest import Test
from bunch import Bunch


directory = "microbenchmarks/"
benchmark_file = 'tests.yml'


def get_json(filename):
	json_data = open(filename)
	data = json.load(json_data)
	json_data.close()
	return data

def get_tests(time_to_complete = 1):

	files = [line.strip() for line in open(directory + benchmark_file, 'r') if line[0] != "#" and len(line) > 1]
	config = open_yaml("microbenchmarks/config.yml")
	files = open_yaml(directory + benchmark_file)["tests"]

	tests =[]
	for f in files:
		print f
		data = open_yaml(directory + f)
		data =  data["commands"]
		commands = [Bunch(**command) for command in data]
		test = Test(f, commands, config, time_to_complete)
		tests.append(test)
	return tests
	
def run(time_to_complete = 1, virtual = True):
	tests = get_tests(time_to_complete)
	if not virtual:
		master = jnd.JNDArduino();
		master.open()
		time.sleep(2)
	for t in tests:
		print t,
		schedule = t.get_sequence()
		Us, Qs, Ts, timescale = scheduler.calculate_edf_cbs(schedule, scheduler.atmega328_k)
		schedule = scheduler.elongate(schedule, timescale)
		schedule = scheduler.cbs(schedule, Us, Ts)
		for job in schedule:
			print job
			pass
		if not virtual:
			print "|| EDF perceptual error: ", "{:2.2f}%".format(scheduler.send(master, schedule))

	if not virtual:
		time.sleep(2)
		master.close()


def main(): 
	# t = 0.00178
	# print t
	# run(time_to_complete = t)
	print "RUNNING PERCEPTUAL TESTS"
	t = 1.29
	# # print t
	run(time_to_complete = t)

	# t = 1.3
	# print t
	# run(time_to_complete = t)

	# t = 5
	# print t
	# run(time_to_complete = 1)



def open_yaml(filename):
	with open(filename) as f: 
 		dataMap = yaml.load(f)
	return dataMap
		
if __name__ == "__main__": main()


