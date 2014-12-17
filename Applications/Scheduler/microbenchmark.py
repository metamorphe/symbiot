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
		# print f
		data = open_yaml(directory + f)
		data =  data["commands"]
		commands = [Bunch(**command) for command in data]
		test = Test(f, commands, config, time_to_complete)
		tests.append(test)
	return tests
	
def run_compare(time_to_complete = 1, virtual = True, time_morph = 1, Q_reduce = 16):
	tests = get_tests(time_to_complete)
	master = None
	for t in tests:
		print t

		addr_list = t.get_addr_list()
		print "AN:", len(addr_list),

		schedule = t.get_sequence()
		schedule = scheduler.psf(schedule, time_morph, Q_reduce, True)
		perfect_record = scheduler.send(master, schedule, addr_list, virtual)

		schedule = t.get_sequence()
		schedule = scheduler.psf(schedule, time_morph, Q_reduce)
		psf_record = scheduler.send(master, schedule, addr_list, virtual)

		schedule = t.get_sequence()
		schedule = scheduler.cbsedf(schedule, time_morph, Q_reduce)
		edf_record = scheduler.send(master, schedule, addr_list, virtual)
	
		n = min(len(psf_record), len(perfect_record), len(edf_record))


		diff = np.absolute(perfect_record[:n] - psf_record[:n]) 
		# print np.sum(diff)
		print "PTS:", 20 * np.log10(n * 999 / np.sqrt(np.sum(diff))),
		print "PTS2:", np.sum(diff)/n,

		diff = np.absolute(perfect_record[:n] - edf_record[:n])
		# print np.sum(diff) 
		print "CBS:", 20 * np.log10(n * 999 / np.sqrt(np.sum(diff))),
		print "CBS2:", np.sum(diff)/n

	

def run(time_to_complete = 1, virtual = True, time_morph = 1, Q_reduce = 16):
	tests = get_tests(time_to_complete)
	master = None
	if not virtual:
		master = jnd.JNDArduino();
		master.open()
		time.sleep(2)
	for t in tests:
		print t
		schedule = t.get_sequence()
		schedule = scheduler.psf(schedule, time_morph, Q_reduce)
		# for i, job in enumerate(schedule):
		# 	print i, job
		# 	pass
		while True:
			scheduler.send(master, schedule, False, virtual)

	if not virtual:
		for i in range(0, 32):
			master.actuate(i, 0)
		time.sleep(2)
		master.close()


def bad_running(time_to_complete = 1, virtual = True, time_morph = 1, Q_reduce = 16):
	tests = get_tests(time_to_complete)
	master = None
	addr_list = None
	if not virtual:
		master = jnd.JNDArduino();
		master.open()
		time.sleep(2)
	for t in tests:
		print t
		schedule = t.get_sequence()
		schedule = scheduler.cbsedf(schedule, time_morph, Q_reduce)
		edf_record = scheduler.send(master, schedule, addr_list, virtual)

		# for i, job in enumerate(schedule):
		# 	print i, job
		# 	pass
		while True:
			scheduler.send(master, schedule, None, False, virtual)

	if not virtual:
		for i in range(0, 32):
			master.actuate(i, 0)
		time.sleep(2)
		master.close()
	

import sys, getopt

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
	print "Qs", "{:2.0f}".format(q_reduce),
	# print "at", "{:3.2f}%".format(q_reduce/16.*100) 
	

	# if not bad_run:
	# 	run(time_to_complete, is_virtual, time_morph, q_reduce)
	# else:
	# 	bad_running(time_to_complete, is_virtual, time_morph, q_reduce)
	run_compare(time_to_complete, is_virtual, time_morph, q_reduce)
	# run_compare(time_to_complete, is_virtual, time_morph, 1)
	# run_compare(time_to_complete, is_virtual, time_morph, 2)
	# run_compare(time_to_complete, is_virtual, time_morph, 5)
	# run_compare(time_to_complete, is_virtual, time_morph, 10)
	# run_compare(time_to_complete, is_virtual, time_morph, 20)
	# run_compare(time_to_complete, is_virtual, time_morph, 30)
	# run_compare(time_to_complete, is_virtual, time_morph, 40)
	# run_compare(time_to_complete, is_virtual, time_morph, 48)




def open_yaml(filename):
	with open(filename) as f: 
 		dataMap = yaml.load(f)
	return dataMap
		
if __name__ == "__main__":
   main(sys.argv[1:])

