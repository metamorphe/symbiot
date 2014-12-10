#quantizing on the fixed-time chunk is one way of avoiding splitting tasks
#each is a fixed time chunk. <actuation time = WCET> roughly equal for each actuator. 

# we know beforehand that tasks have a low WCET variance, however the commands change at run time, as a result of how objects are being scheduled.

#real-time scheduling
import jnd_arduino as jnd
import time, numpy as np
import Queue, sys, operator
from quanta_schedule import QuantaSchedule
sys.path.append('lib')
from job import Job
from quanta import Quanta



atmega328_k = 0.578 # rate of execution Hz

def histogram(elements):
	hist = {}
	for el in elements:
		if hist.has_key(el.priority):
			hist[el.priority].append(el)
		else:
			hist[el.priority] = [el]
	return hist


def edf_params(schedule):
	quanta = histogram(schedule)
	itemized_schedule = sorted(quanta.items(), key=operator.itemgetter(0))
	i = 0
	max_requests = -1
	max_collisions = []
	for n, q in itemized_schedule:
		if len(q) > max_requests:
			max_requests = len(q)
			max_collisions = []
			max_collisions.append(i)
			max_quanta = q

		if len(q) == max_requests:
			max_collisions.append(i)

		i += 1

	t_s = [itemized_schedule[idx + 1][0] - itemized_schedule[idx][0] for idx in max_collisions if idx < len(itemized_schedule)-1]
	collision_time = min(t_s)
	total_time = itemized_schedule[-1][0] - itemized_schedule[0][0]
	return collision_time, total_time, max_requests
	
def calculate_edf_cbs(schedule, k):
	''' Content-based selection of Us and Ts parameters'''
	t_s, t_e, m_col = edf_params(schedule) # in seconds
	# print t_s, t_e, m_col 
	Ts = k * m_col /1000. #bandwidth
	nT = Ts * t_e / t_s
	time_scale = nT/ t_e


	# time_scale = (Ts * ) / t_e  # scale so that collision space meets minimum val

	Qs = m_col  
	Us = Qs/Ts
	
	return Us, Qs, Ts, time_scale

def elongate(schedule, scalar):
	for job in schedule:
		job.longer(scalar)
	return schedule


def possess(dead_job, generations):
	child = find(generations, dead_job.addr)
	age_diff = chid.time - dead_job.time
	energy_diff = child.value - dead_job.value


def cbs(schedule, Qs, Ts):
	''' Implements a bandwidth-divided server and enqueues Jobs 
		Us is server bandwidth per time period Ts
	'''
	
	qs = QuantaSchedule(schedule, Qs, Ts)
	# print qs

	qs.clean()
	# print qs

	for q in qs.quanta:
		# print q
		# if q.id >= 288:
		# 	print q
		# 	for j in q.jobs:
		# 		print "\t", j
		pass
		
	return qs.to_schedule()

def psf(schedule, time_morph = 1, Q_reduce = 16):
	# Us, Qs, Ts, timescale = calculate_edf_cbs(schedule, atmega328_k)
	# print "Us", Us, "Qs", Qs, "Ts", Ts, timescale
	
	# ARDUINO CAPACITY, EDF PARAMS
	
	Us = 1. / atmega328_k
	Qs = 16.
	Ts = Qs / Us / 1000
	
	# ADJUSTMENTS
	t_s, t_e, m_col = edf_params(schedule) # in seconds
	nT = Ts * t_e / t_s

	print "minimum time", nT, "current_time", t_e,

	timescale = nT/ t_e * time_morph 
	print "scale", timescale

	# ARTIFICIAL SIMULATION
	Qs = Q_reduce

	schedule = elongate(schedule, timescale)
	cbs_schedule = cbs(schedule, Qs, Ts)

	return cbs_schedule


def to_commands(schedule, priority_type = "edf", param = None):
	# get alpha value
	q = Queue.PriorityQueue(maxsize=0)
	for job in schedule: 
		if param:
			q.put(job.set_priority(priority_type))
		else:
			q.put(job.set_priority(priority_type, param))

	compiled_commands = []
	while not q.empty():
		compiled_commands.append(q.get())
	return compiled_commands

# send behavior
def send(ard, base, verbose=False):
	if verbose: 
		print "SCHEDULED SEND"
	
	# Need to put this on a separate thread
	t0 = time.time()
	log = []
	
	for job in base:
		next_time = job.metadata.time # delays for x ms
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






