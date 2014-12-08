#quantizing on the fixed-time chunk is one way of avoiding splitting tasks
#each is a fixed time chunk. <actuation time = WCET> roughly equal for each actuator. 

# we know beforehand that tasks have a low WCET variance, however the commands change at run time, as a result of how objects are being scheduled.

#real-time scheduling
import jnd_arduino as jnd
import time, numpy as np
import Queue, sys
sys.path.append('lib')
from job import Job



atmega328_k = 0.578 # rate of execution Hz

def histogram(elements):
	histogram = {}
	for el in elements:
		if hist[el.priority]:
			hist[el.priority].append(el)
		else:
			hist[el.priority] = []
	print histogram


def edf_params(schedule):
	quanta = histogram(schedule)
	max = -1
	for i, quantum in enumerate(quanta):
		if len(quantum) > max:
			max = len(quantum)
			max_quantum = quantum

	collision_time = max_quantum[-1].time - max_quantum[0].time 
	total_time = schedule[-1].time - schedule[0].time

	return collision_time, total_time, max_collisions

def calculate_edf_cbs(schedule, k):
	''' Content-based selection of Us and Ts parameters'''
	t_s, t_e, m_col = edf_params(schedule)
	c_i = k * m_col #bandwidth
	t_i = c_i * t_e / t_s # scale so that collision space meets minimum val
	return c_i, t_i 


def cbs(schedule, Us, Ts, k):
	''' Implements a bandwidth-divided server and enqueues Jobs 
		Us is server bandwidth per time period Ts
	'''
	schedule = histogram(Ts)
	# filter commands and apply dither and resurrect
	needed_bandwidth = (len(server_chunk) - (Us  / k))
	for i, server_chunk in enumerate(schedule):
		server_chunk = clean_server_chunk(server_chunk, i, Us, k)

	schedule = commands
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






