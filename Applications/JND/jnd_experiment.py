# from pylab import *
import random, os
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

class Experiment:
	
	participantNumber = 0

	def __init__(self):
		# self.participant = participantNumber
		# Experiment.participantNumber += 1 #change participant counter
		self.actuators = ["LED", "heatpad"]
		print "Press 'r' to start the first actuator" #runs actuator_setup
		self.ranges = []
		self.values = []
		for i in range(0, 1001):
			self.values.append(i)
		self.query = random.choice(self.values)

	#sets up new actuator
	def actuator_setup(self):
		if len(self.actuators) != 0:
			# self.new_actuator(self.participant)
			self.ranges = []
			self.values = []
			for i in range(0, 1001):
				self.values.append(i)
			self.next_range()
		else:
			print "Experiment complete!"
			#remove current actuator from list of actuators
			self.actuators.remove(self.actuator)


	#creates file structure Actuator/participantNumber
	def new_actuator(self, participantNumber):
		self.actuator = random.choice(actuators)
		if not os.path.exists(actuator):
			os.makedirs(actuator)
		participant = 'Participant'
		participant += str(self.participantNumber)
		participantFolder = actuator + '/' + participant + '/'
		os.makedirs(participantFolder)



	#sets query; resets limit and jnd_range
	def next_range(self):
		#choose random query
		if len(self.values) != 0:
			self.query = random.choice(self.values) #NOT WORKING
			self.lower_limit = self.upper_limit = False
			self.jnd_range = []
			print "Start next range"
			print "Query is actuating to ", self.query
			return self.query
		else:
			print "Current actuator complete"
			self.ranges = sorted(self.ranges, key=itemgetter(0))
			#visualization
			self.visualize()


	#change actuated value by specified change
	def change_value(self, old_value, change):
		actuate = old_value + change
		if actuate < 0:
			actuate = 0
		elif actuate > 1000:
			actuate = 1000
		print "Actuating to ", actuate
		return actuate



	#set/reset limits
	def set_lower_limit(self, value):
		self.lower_limit = value
		print "lower limit set to ", value
	def set_upper_limit(self, value):
		self.upper_limit = value
		print "upper limit set to ", value



	#get values of limits
	def get_lower_limit(self):
		return self.lower_limit
	def get_upper_limit(self):
		return self.upper_limit


	def get_query(self):
		return self.query


	#adds range to array of ranges and removes from values
	def remove_jnd_range(self):
		lower = self.get_lower_limit()
		upper = self.get_upper_limit()
		if lower != False and upper != False:
			self.jnd_range = [lower, upper]
			print "JND RANGE ", self.jnd_range

			#ranges are appending correctly
			self.ranges.append([self.query, self.jnd_range])

			#values isn't updating correctly
			self.values = self.update_values()
			print "Range added"
			print "Press 'n' to start next range "


	def update_values(self):
		# print "Pre: ", self.values
		down, up = self.fifty()
		# print "Range that should be removed ", down, up
		up += 1 #correcting limits
		for j in range(down, up):
			#index of the candidate value
			try:
				self.values.remove(j)
			except ValueError:
				pass
		# print "Post: ", self.values
		return self.values


	def fifty(self):
		down = self.jnd_range[0]
		# print "jnd range[0] ", down
		up = self.jnd_range[1]
		# print "jnd range[1] ", up

		fifty_up = (up - self.query) / 2
		fifty_up += self.query
		# print "fifty up ", fifty_up
		fifty_down = (down - self.query) / 2
		fifty_down += self.query
		# print "fifty down ", fifty_down

		fifty_range = [fifty_down, fifty_up]
		# print "fifty range ", fifty_range
		return fifty_range


	def visualize(self):
		self.values = [[100, [80, 120]], [500, [121, 1000]]]
		self.x = []
		self.y = []
		for i in range(len(self.values)):
			#upper limits of ranges
			self.x.append(self.values[i][1][1])
			#intensity levels
			self.y.append(i)
		# for x in self.x:
		# 	self.results = self.func(self.x, self.y)
		# print self.results

		plt.scatter(self.x, self.y)
		plot.xticks
		plt.show()

		# self.x = np.array(self.x)
		# self.y = np.array(self.y)

		# popt, pcov = curve_fit(self.func, self.x, self.y, [100,400,0.001,0])
		# print popt



""" THESE SHOULD NOT BE EXPERIMENT CLASS FUNCTIONS """

def fit_model(x, y, func):
	popt, pcov = curve_fit(func, x, y)
	return popt, pcov

def stephen_power_law(x, k, a, c):
    return k * np.power(x, a) + c

def plot(x, y, y_predicted):
	plt.figure()
	plt.plot(x, y, 'ko', label="Original Pyshcophysics Data")
	plt.plot(x, y_predicted, 'r-', label="Stephen's Power Curve")
	plt.legend()
	plt.show()

""" YOUR EXPERIMENT SHOULD RETURN THE FOLLOWING: """
# five ranges identified, upperbounds used
magnitude =  [0, 100, 300, 400, 800, 1000]
brightness = [0, 1, 2, 3, 4, 5]

model, error = fit_model(magnitude, brightness, stephen_power_law)
plot(magnitude, brightness, stephen_power_law(magnitude, *model))
# => a = 0.19490441, error = 0.00044376



# experiment = Experiment()
# print experiment.func(1, 0.5, 0)