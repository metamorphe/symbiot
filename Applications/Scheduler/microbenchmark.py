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
import numpy as np
import sys, getopt


directory = "microbenchmarks/"
benchmark_file = 'stagger.yml'


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
		# print f
		data = open_yaml(directory + f)
		data =  data["commands"]
		commands = [Bunch(**command) for command in data]
		test = Test(f, commands, config, time_to_complete)
		tests.append(test)
	return tests

def evaluate(schedule):
	n = min(len(psf_record), len(perfect_record), len(edf_record))

	diff = np.absolute(perfect_record[:n] - psf_record[:n]) 
	MSE = (np.sum(np.power(diff, 2))) / n
	error = 20 * np.log10(999) - 10 * np.log10(MSE)
	print ",", error,

	diff = np.absolute(perfect_record[:n] - edf_record[:n])
	MSE = (np.sum(np.power(diff, 2))) / n
	error = 20 * np.log10(999) - 10 * np.log10(MSE)
	print ",", error


def send(arduino):


def run_arduino(schedule):
	controller = None
	controller = jnd.JNDArduino();
	controller.open()
	send(controller, schedule)
	controller.turn_all_off()
	controller.close()


def run(tests):	
	for t in tests:
		print t
		addr_list = t.get_addr_list()
		schedule = t.get_sequence()		
		schedule = scheduler.psf(schedule, time_morph, Q_reduce, True)
		base = scheduler.send(master, schedule, addr_list, virtual, False)

		schedule = t.get_sequence()
		scheduleA = scheduler.psf(schedule, time_morph, Q_reduce)
		schedule = t.get_sequence()
		scheduleB = scheduler.cbsedf(schedule, time_morph, Q_reduce)
		
		print evaluate(base, scheduleA)
		print evaluate(base, scheduleB)



def macrobenchmark( time_to_complete = 1):
	
	config = open_yaml("microbenchmarks/config.yml")
	tests = []	
	data =[]

	f = "MACROBENCHMARK " 
	for i in range (0, 7):
		data.append({"addr":i, "behavior_id": 39, "flavor_id":5, "start" : 0})
	for i in range (0, 16):
		data.append({"addr":i, "behavior_id": 10, "flavor_id":5, "start" : 0})
	for i in range (0, 30):
		data.append({"addr":i, "behavior_id": 16, "flavor_id":5, "start" : 5})
	for i in range (0, 2):
		data.append({"addr":i, "behavior_id": 12, "flavor_id":5, "start" : 5})

	step = 0.0001
	for i in range (0, 30):
			data.append({"addr":i, "behavior_id": 16, "flavor_id":5, "start" : 8 + i * step})

	data.append({"addr":i, "behavior_id": 13, "flavor_id":5, "start" : 8 + i * step})


	commands = [Bunch(**command) for command in data]
	test = Test(f, commands, config, time_to_complete)
	tests.append(test)
	
	return tests

def microbenchmark_budget(behavior_id, n=35, step=0):
	config = open_yaml("microbenchmarks/config.yml")
	scales = [11, 15, 20, 25, 30, 35, 40, 45]	
	
	tests = []

	for n in scales: 
		data = []
		f = "$$$/B" + str(behavior_id) + "/" + str(n) + "/" + 0

		for i in range (0, n):
			data.append({"addr": i, "behavior_id": behavior_id, "flavor_id": 5, "start" : i * step})

		commands = [Bunch(**command) for command in data]
		test = Test(f, commands, config, time_to_complete)
		tests.append(test)
	
	return tests



def microbenchmark_scale(behavior_id, q_s=10, step=0):
	config = open_yaml("microbenchmarks/config.yml")
	scales = [11, 15, 20, 25, 30, 35, 40, 45]	
	tests = []

	for n in scales: 
		data =[]

		f = "SCALE/B" + str(behavior_id) + "/" + str(n) + "/" + 0

		for i in range (0, n):
			data.append({"addr": i, "behavior_id": behavior_id, "flavor_id": 5, "start" : i * step})

		commands = [Bunch(**command) for command in data]
		test = Test(f, commands, config, time_to_complete)
		tests.append(test)
	
	return tests


def main(argv):
	is_virtual = False
	time_to_complete = None
	q_reduce = 16
	bad_run = False
	time_morph = 1


	try:
		opts, args = getopt.getopt(argv,"vbhs:q:t")
	except getopt.GetoptError:
		print 'microbenchmark.py -t <time_to_complete> -v <virtual> -q <q_s> -s <time_scale>'
		sys.exit(2)
	# print opts
	for opt, arg in opts:
		# print opt, arg
		if opt == '-h':
			print 'microbenchmark.py -t <time_to_complete> -v <virtual>'
			sys.exit()
		elif opt in ("-q", "--qreduce"):
			q_reduce = float(arg)
		elif opt in ("-s", "--scale"):
			time_morph = float(arg)
		elif opt in ("-v", "--virtual"):
			is_virtual = arg == ""
		elif opt in ("-b", "--bad"):
			bad_run = arg == ""

	# print "RUNNING PERCEPTUAL TESTS",
	# if is_virtual:
	# 	print "VIRTUALLY",
	# else:
	# 	print "TO ARDUINO",

	if not time_to_complete:
		time_to_complete = 1.29

	print "T:", time_to_complete * time_morph, "(S)", 
	# print "T:", time_to_complete, "(S)", 
	# print " x ", time_morph,
	print "Qs", "{:2.0f}".format(q_reduce)
	# print "at", "{:3.2f}%".format(q_reduce/16.*100) 
	




def open_yaml(filename):
	with open(filename) as f: 
 		dataMap = yaml.load(f)
	return dataMap
		
if __name__ == "__main__":
   main(sys.argv[1:])

