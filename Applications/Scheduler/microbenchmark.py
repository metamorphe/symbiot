# Runs microbenchmark tests

import Queue, math, json, sys
sys.path.append('lib')
from job import Job
from pprint import pprint
import jnd_arduino as jnd
import scheduler as scheduler
import  time
from microtest import Test
from bunch import Bunch

directory = "microbenchmarks/"
benchmark_file = 'tests.yaml'


def get_json(filename):
	json_data = open(filename)
	data = json.load(json_data)
	json_data.close()
	return data

def get_tests(time_to_complete = 1):
	files = [line.strip() for line in open(directory + benchmark_file, 'r') if line[0] != "#" and len(line) > 1]
	
	tests = []
	for f in files:
		data = get_json(directory + f)
		commands = []
		for d in data:
			metadata = Bunch()
			metadata.addr = d["addr"]
			metadata.f_id = d["flavor_id"]
			metadata.b_id = d["behavior_id"]
			metadata.t0 = d["t0"]
			commands.append(metadata)
		test = Test(f, commands, time_to_complete)
		tests.append(test)
	return tests

	
def run(time_to_complete = 1):
	tests = get_tests(time_to_complete)
	master = jnd.JNDArduino();
	master.open()
	time.sleep(2)
	for test in tests:
		print test,
		print "|| EDF perceptual error: ", "{:2.2f}%".format(scheduler.send(master, test.sequence, scheduler.edf))

		# test.print_sequence()
	time.sleep(2)
	master.close()

def main(): 
	run(time_to_complete = 1.53)
if __name__ == "__main__": main()


