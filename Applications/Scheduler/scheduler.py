#really what is happening is the scheduler is not being made different. 
#its turning commands into sparse representations

#quantizing on the fixed-time chunk is one way of avoiding splitting tasks
#each is a fixed time chunk. <actuation time = WCET> roughly equal for each actuator. 

# we know beforehand that tasks have a low WCET variance, however the commands change at run time, as a result of how objects are being scheduled.

#real-time scheduling
import jnd_arduino as jnd
import time, numpy as np
import expresso_api as api
import Queue, math


class Bunch(dict):
    def __init__(self,**kw):
        dict.__init__(self,kw)
        self.__dict__ = self

	def __str__(self):
	    state = ["%s=%r" % (attribute, value)
	             for (attribute, value)
	             in self.__dict__.items()]
	    return '\n'.join(state)

# send behavior

def d_dt(commands):
	a = np.array(commands, dtype=np.float).T
	time_diff = np.convolve(a[0], [1, -1])#[1:-1] # d/dt, remove extra element
	
	# END COMMANDS WITH MAG 0
	time_diff[-1] = 0
	time_diff = time_diff[1:]
	a[1][-1] = 0

	diff_commands = np.array([time_diff, a[1]])
	return diff_commands.T


def send_behavior(ard, addr, id,  velocity=1):
	print "SYNCHRONOUS SEND"
	commands = api.get_commands(id, velocity)
	# convert to differential time
	diff_commands = d_dt(commands)
	t0 = time.time()

	log = []

	for t, v in diff_commands:
		# print "send", "t: %5.0f" % ((time.time() - t0) * 1000), "delay:%5.0f" % (t * velocity), "mag:%5.0f" % v
		ard.actuate(addr, v)
		log.append(Job(id, time.time() - t0, v , addr));
		print "COMMAND @", "{:3.2f}".format(time.time() - t0), "to", "{:1.0f}".format(addr) + ":" + "{:3.0f}".format(v )
		time.sleep(t) # delays for x ms
	
	# END BUFFER
	ard.actuate(addr, 0)
	time.sleep(0.5)
	print "SYNCHRONOUS END"
	return log


def microbenchmark(ids, velocity=1):
	quanta = 5;
	q = Queue.PriorityQueue(maxsize=0)
	for id, addr in ids:
		for t, v in api.get_commands(id, velocity):

			if math.isnan(v):
				q.put(Job(id, t, 0, addr))
			else:
				q.put(Job(id, t, v, addr))
	return q


def scheduled_send(ard, base):
	print "SCHEDULED SEND"
	# Need to put this on a separate thread
	t0 = time.time()
	log = []
	# while not q.empty():
	for job in base:
		# next_job = q.get()
		next_time = job.priority # delays for x ms
		current_time = time.time() - t0
		
		while(next_time > current_time):
			# print "Sleeping for", next_time - current_time
			time.sleep((next_time - current_time))
			current_time = (time.time() - t0)


		# if next_job.description:
		print "COMMAND @", "{:3.0f}ms".format(current_time * 1000), "to", job
		ard.actuate(job.addr, job.description)
		log.append(Job(id, time.time() - t0, job.description, job.addr));

	print "SCHEDULED END"
	return log

def all(ard, command):
	for i in range(0, 10):
		ard.actuate(i, command)

def command_stats(q):
	collisions = {}
	while not q.empty():
		next_job = q.get()
		# print next_job.priority
		try:
			collisions[next_job.priority].append(next_job)
		except KeyError, e:
			collisions[next_job.priority] = []
	# print collisions.iteritems()
	
	conflicts = dict((timestamp, jobs) for timestamp, jobs in collisions.iteritems() if len(jobs) > 2)
	sum = 0
	for t, c in conflicts:
		sum += c
	print "Collisions", sum

def calc_error(base, logs = []):
	print len(base)
	error = []
	for l in logs:
		error.append(sum(base - l))
	return error

def send(ard, addr, behavior, speed):
	commands = []
	for i in range(0, 10):
		commands.append((3, i))

	q = microbenchmark(commands, speed)
	base = []
	while not q.empty():
		base.append(q.get())
	scheduled = scheduled_send(ard, base)
	return calc_error(np.array(base), [np.array(scheduled)])


def main():

	# and of course you can read/write the named
	# attributes you just created, add others, del
	# some of them, etc, etc:
	
	velocity = 6
	mc = Bunch(master=jnd.JNDArduino())
	behaviors = Bunch(transmission=23, ekg=8, raindrops=18, lighthouse=12, easy=3)
	actuators = Bunch(red_led=5, green_led=3, yellow_led=6)
	
	# q = microbenchmark([(behaviors.transmission, actuators.green_led), (behaviors.transmission, actuators.red_led), (behaviors.transmission, actuators.yellow_led)])



	# # MAIN EXECUTION LOOP
	mc.master.open()
	time.sleep(1)

	# mc.master.actuate(actuators.green_led, 1000)
	# synchronous = send_behavior(mc.master, actuators.green_led, behaviors.easy, velocity)
	mc.master.flush()

	print send(mc.master, actuators.green_led, behaviors.easy, 3)
	
	time.sleep(1)
	mc.master.close()
	return mc.master

	# while True:
	# 	pass
	# mc.master.close()


	# print calc_error(np.array(base), [np.array(scheduled)])
	# print calc_error(np.array(base), [np.array(synchronous), np.array(scheduled)])



class Job(object):
    def __init__(self, id, priority, description, addr):
        self.priority = priority
        self.description = description
        self.behavior_id = id
        self.addr = addr
        return
    def __cmp__(self, other):
        return cmp(self.priority, other.priority)
    def __str__(self):
    	return "{:1.0f}".format(self.addr) + ":" + "{:3.0f}".format(self.description)
    def __sub__(self, other):
    	return abs(self.priority - other.priority)

ard = None
if __name__ == "__main__": ard = main()


