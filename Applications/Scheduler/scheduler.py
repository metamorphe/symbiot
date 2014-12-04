#quantizing on the fixed-time chunk is one way of avoiding splitting tasks
#each is a fixed time chunk. <actuation time = WCET> roughly equal for each actuator. 

# we know beforehand that tasks have a low WCET variance, however the commands change at run time, as a result of how objects are being scheduled.

#real-time scheduling
import jnd_arduino as jnd
import time, numpy as np
import Queue
from job import Job
def edf(sequence):
	# get alpha value
	q = Queue.PriorityQueue(maxsize=0)
	for job in sequence: 
		q.put(job)
	
	compiled_commands = []
	while not q.empty():
		compiled_commands.append(q.get())
	return compiled_commands

# send behavior
def send(ard, base, scheduling_algorithm,  verbose=False):
	if verbose: 
		print "SCHEDULED SEND"
	
	base = scheduling_algorithm(base)
	
	# Need to put this on a separate thread
	t0 = time.time()
	log = []
	
	for job in base:
		next_time = job.priority # delays for x ms
		current_time = time.time() - t0
		
		while(next_time > current_time):
			# print "Sleeping at", "{:3.0f}ms".format(current_time * 1000), "for", "{:3.0f}ms".format((next_time - current_time) * 1000)
			time.sleep((next_time - current_time))
			current_time = (time.time() - t0)
		if verbose:
			print "COMMAND @", "{:3.0f}ms".format(current_time * 1000), "to", job

		ard.actuate(job.metadata.addr, int(job.value))
		log.append(Job(job.metadata, time.time() - t0, job.value));

	if verbose:
		print "SCHEDULED END"
	return calc_error(np.array(base), np.array(log))

def calc_error(base, log):
	return sum(base - log) / base.size * 100






