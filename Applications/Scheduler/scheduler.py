#quantizing on the fixed-time chunk is one way of avoiding splitting tasks
#each is a fixed time chunk. <actuation time = WCET> roughly equal for each actuator. 

# we know beforehand that tasks have a low WCET variance, however the commands change at run time, as a result of how objects are being scheduled.

#real-time scheduling
import jnd_arduino as jnd
import time, numpy as np
import Queue, sys, operator
sys.path.append('lib')
from job import Job



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

def cbs(schedule, Us, Ts):
	''' Implements a bandwidth-divided server and enqueues Jobs 
		Us is server bandwidth per time period Ts
	'''
	for job in schedule:
		job.set_priority("cbs", Ts)

	quanta = histogram(schedule)
	quanta = sorted(quanta.items(), key=operator.itemgetter(0))
	
	Qs = Us * Ts
	# filter commands and apply dither and resurrect
	idx = 0
	for n, q in quanta:
		# print n, len(q)
		if len(q) > Qs:
			# print "oversubscribed"
			pass
		else:
			# print idx, "is utilized", "{:3.2f}%".format(len(q) / Qs * 100) 
			pass
		idx += 1

	# 	server_chunk = clean_server_chunk(server_chunk, i, Us, k)



	# histogram back to schedule
	schedule = []
	for n, q in quanta: 
		schedule.append(q)
	schedule = sum(schedule, [])

	return schedule

def server_chunk_clean(server_chunk, i, Us, k):
	needed_bandwidth = (len(server_chunk) - (Us  / k))
	cut_out = server_chunk[0:-needed_bandwidth]
	for job in cut_out:
		if job.isHard(): 
			dither(job, i)
		else:
			resurrect(job, i)

	return server_chunk

def psf(schedule):
	Us, Ts = calculate_edf_cbs(schedule, atmega328_k)
	cbs_schedule = cbs(schedule, Us, Ts, atmega328_k)
	psf = dither(schedule)
	psf = resurrect(schedule)
	psf = diligent_server(schedule)
	return psf

def dither(job):
	''' Moves energy evenly across synchronous elements over time '''
	return schedule

def resurrect(schedule):
	''' 
	Graveyard jobs are resurrected and benignly possess 
	their children's offspring until its mortal deed can be accomplished.
	'''
	return schedule

def diligent_server(schedule):
	'''
	When the server is idle and has some extra bandwidth, it goes ahead and
	runs the scheduling algorithm ahead of itself
	'''
	return schedule


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
			print "Sleeping at", "{:3.0f}ms".format(current_time * 1000), "for", "{:3.0f}ms".format((next_time - current_time) * 1000)
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






