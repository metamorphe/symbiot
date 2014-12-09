import expresso_api as api
import math, copy
from job import Job
import numpy as np

def find_nearest(array, query):
	idx = (np.abs(array - query)).argmin()
	return idx

def harden(sequence):
		'''
		Converts a behavior B into hard and soft tasks.
		Hardness attribute added to the Job definition. 
		'''
		hardening_threshold_max = 990
		hardening_threshold_min = 4

		original_commands = np.array(sequence, dtype=np.float).T
		
		jnd_diff = np.convolve(original_commands[1], [1, -1])#[1:-1] # d/dt, remove extra element
		jnd_diff = jnd_diff[:-1]

		minmax = np.absolute(jnd_diff)
		# start and end are always min and max
		minmax[0] = 1000 
		minmax[-1] = 1000
		min_max_mask = np.logical_not(np.logical_or(minmax > hardening_threshold_max, minmax < hardening_threshold_min))

		timestamps = original_commands[0]
		temporal_mask = timestamps.copy()
		temporal_mask[min_max_mask] = 10



		hardness = [abs(i - find_nearest(temporal_mask, timestamps[i])) for i, h in enumerate(jnd_diff)]
	
		
		hardened_commands = np.vstack([original_commands, hardness])
		return hardened_commands.T
		# print temporal_mask.T
		# return np.vstack([hardness, temporal_mask]).T

class Test:
	def __init__(self, name, commands, config, time_to_complete = None):
	    self.name = name
	    self.config = config
	    
	    self.commands = commands
	    self.time = time_to_complete
	    self.sequence = self.get_sequence()
	    self.collision_rate = self.collisions()
	   
	    return

	def __str__(self):
		time = self.sequence[-1].priority

		# time *= self.velocity
		return self.name + "|| collision_rate: " + str(self.collision_rate) + "|| N: " + str(len(self.sequence)) + "|| T: " + str(time) 

	def bulls_eye(self, addr, sequence):
		'''
		Calculates the distance of an actuator from its perceptual center.
		Adds a distance attribute to the Job definition.
		'''
		# uniform distance
		d = self.config["board"][addr]["distance"]
		return [(t, v, h, d) for t, v, h in sequence]

	def print_sequence(self):
		for s in self.sequence:
			print s

	def get_sequence(self):
		for c in self.commands:
			c.alpha = api.get_flavor(c.flavor_id)["alpha"]
			c.alpha = 0.3


		if self.time == None:
			self.velocity = 1
		else:
			c = self.commands[-1]
			t, v = api.get_commands(c.behavior_id, alpha = c.alpha)[-1]
			self.velocity = self.time / t

		sequence = []
		for c in self.commands:
			subsequence = api.get_commands(c.behavior_id, alpha = c.alpha)
			subsequence = harden(subsequence)
			subsequence = self.bulls_eye(c.addr, subsequence)

			for t, v, h, d in subsequence:
				c.hardness = h
				c.locality = d
				c.time = t * self.velocity + c.t0

				if math.isnan(v):
					sequence.append(Job(c, t * self.velocity + c.t0, 0))
				else:
					sequence.append(Job(c, t * self.velocity + c.t0, v))

		return sequence

	def collisions(self):
		commands_cpy = copy.deepcopy(self.sequence)
		collisions = {}
		size = len(self.sequence)
		for c in commands_cpy: 
			try:
				collisions[str(c.priority)].append(c)
			except KeyError, e:
				collisions[str(c.priority)] = [c]

		# count collisions
		conflicts = dict([(timestamp, len(jobs)) for timestamp, jobs in collisions.iteritems() if len(jobs) > 2])
		# sum of collisions
		sum = 0.
		for t, c in conflicts.iteritems():
			sum += c

		return sum/size
