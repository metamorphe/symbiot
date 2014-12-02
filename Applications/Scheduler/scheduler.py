#really what is happening is the scheduler is not being made different. 
#its turning commands into sparse representations

#quantizing on the fixed-time chunk is one way of avoiding splitting tasks
#each is a fixed time chunk. <actuation time = WCET> roughly equal for each actuator. 

# we know beforehand that tasks have a low WCET variance, however the commands change at run time, as a result of how objects are being scheduled.

#real-time scheduling
import jnd_arduino as jnd
import time, numpy as np
from job import Job





# send behavior
def send(ard, base):
	print "SCHEDULED SEND"
	# Need to put this on a separate thread
	t0 = time.time()
	log = []
	# while not q.empty():
	for job in base:
		next_time = job.priority # delays for x ms
		current_time = time.time() - t0
		
		while(next_time > current_time):
			# print "Sleeping for", next_time - current_time
			time.sleep((next_time - current_time))
			current_time = (time.time() - t0)

		print "COMMAND @", "{:3.0f}ms".format(current_time * 1000), "to", job
		ard.actuate(job.addr, job.value)
		log.append(Job(job.behavior_id, job.flavor_id, time.time() - t0, job.value, job.addr));
	print "SCHEDULED END"
	return calc_error(np.array(base), [np.array(log)])

def calc_error(base, logs = []):
	print len(base)
	error = []
	for l in logs:
		error.append(sum(base - l))
	return error






