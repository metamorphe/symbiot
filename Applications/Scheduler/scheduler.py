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


	# print qs

	for q in qs.quanta:
		# print q
		# if q.id >= 288:
		# 	print q
		# 	for j in q.jobs:
		# 		print "\t", j
		pass
		
	return qs


def cbsedf(schedule, time_morph = 1, Q_reduce = 16, is_perfect = False):
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
	if is_perfect:
		Qs = m_col

	schedule = elongate(schedule, timescale)
	qs = cbs(schedule, Qs, Ts)
	qs.squeeky_clean()
	cbs_schedule = qs.to_schedule()

	return cbs_schedule

def psf(schedule, time_morph = 1, Q_reduce = 16, is_perfect = False):
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
	if is_perfect:
		Qs = m_col

	schedule = elongate(schedule, timescale)
	qs = cbs(schedule, Qs, Ts)
	qs.clean()
	cbs_schedule = qs.to_schedule()

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
def send(ard, base, addr_list, virtual=False, verbose=False):
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
		if not virtual:
			ard.actuate(job.metadata.addr, int(job.value))
		log.append(Job(job.metadata, time.time() - t0, job.value));

	if verbose:
		print "SCHEDULED END"

	error = []
	# for addr in addr_list:
		# print "Calculating error for", addr,
		# error = np.concatenate((error, sampled_log(log, addr, atmega328_k / 1000.)))
	# print error
	return error

def find_next(addr, log, ith):
	indices = [i for i, j in enumerate(log) if j.metadata.addr == addr]
	# print i, len(indices)
	# print indices, ith
	if ith > len(indices) - 1 :
		return None
	return log[indices[ith]]

def sampled_log(log, addr, rate):
	# print "sample rate: ",  rate, "n=", len(log), 

	n = len(log)

	T = log[-1].metadata.time
	# print "Total_time", T
	pos_t = 0

	i = 0
	curr_t = 0
	curr_v = 0

	samples = []

	no_more_records = False
	while pos_t < T:
		# print pos_t * 1000, curr_v * 1000
		if pos_t < curr_t or no_more_records:
			samples.append((pos_t, curr_v))
		else:
			i += 1

			next = find_next(addr, log, i)
			if next:
				# print next
				curr_t = next.metadata.time 
				curr_v = next.value
				samples.append((pos_t, curr_v))
			else:
				# print "NO MORE RECORDS"
				no_more_records = True
		pos_t += rate

	# print "E:", int(T/rate) + 1, "/", len(samples)

	# for i, el in enumerate(samples):
	# 	for t, v in el:
	# 		if not v:
	# 			print i, "HELLETH"
	samples = [v for t, v, in samples]
	# print samples
	return np.array(samples)

# def calc_error(base, log):
# 	return sum(base - log) / base.size * 100







