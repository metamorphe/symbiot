from pylab import *
import random, os, unittest, json, sys
from operator import itemgetter
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

class Experiment:
	
	def __init__(self):
		self.participantName = ""
		self.actuators = ["LED"]
		print "Press 's' to turn on the arduino and start the first actuator" #starts actuator setup
		self.ranges = []
		self.values = []
		self.jnd_range = []
		self.actuator = 0
		for i in range(0, 1001):
			self.values.append(i)
		self.query = random.choice(self.values)

	#sets up new actuator
	def actuator_setup(self, username):
		if len(self.actuators) != 0:
			self.participantName = username
			self.new_actuator()
			self.ranges = []
			self.values = []
			for i in range(0, 1001):
				self.values.append(i)
			self.next_range()
		else:
			print "Experiment complete!"


	#creates file structure Actuator/participantName
	def new_actuator(self):
		self.actuator = random.choice(self.actuators)
		if not os.path.exists(self.actuator): # if folder for actuator doesn't exist
			os.makedirs(self.actuator)
			participant = 'Participant'
			participant += str(self.participantName)
			participantFolder = self.actuator + '/' + participant + '/'
			os.makedirs(participantFolder)


	#sets query; resets limit and jnd_range
	def next_range(self):

		#choose random query
		if len(self.values) != 0:
			self.query = random.choice(self.values)
			self.lower_limit = True
			self.upper_limit = False
			self.jnd_range = []
			print "Query is actuating to ", self.query

		else:
			print "Current actuator complete"
			self.actuators.remove(self.actuator) #remove current actuator from list of actuators
			self.query = False
			# self.visualize()
			if len(self.actuators) != 0:
				print "When ready, press 's' to start a new actuator"
			else:
				print "You have finished all actuators. Press 'c' to end the experiment"
		return self.query


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
		print "lower limit set to", self.lower_limit

	def set_upper_limit(self, value):
		self.upper_limit = value
		print "upper limit set to", self.upper_limit



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
		# print "lower is ", lower, "upper is ", upper

		try:
			if (lower != False or lower == 0) and upper != False:

				self.jnd_range = [lower, upper]
				# print "JND RANGE ", self.jnd_range

				#append ranges
				self.ranges.append([self.query, self.jnd_range])
				# print "ranges ", self.ranges

				#remove values
				self.values = self.update_values()
				# print "values ", self.values

				# print "Range added"
				print "Press 'n' to start next range "
		except AttributeError: #if lower or upper not set
			pass


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
		print "fifty range ", fifty_range
		return fifty_range


	def visualize(self):
		
		magnitude = []
		brightness = []

		self.values = sorted(self.values, key=itemgetter(0)) #sort list

		for i in range(len(self.values)):
			#upper limits of ranges
			magnitude.append(self.values[i][1][1])
			#intensity levels
			brightness.append(i)

		magnitude = np.array(magnitude)
		brightness = np.array(brightness)

		plt.figure()
		plt.plot(magnitude, brightness, 'ko', label="Original Psychophysics Data")

		magnitude = [float(xn) for xn in magnitude] #every element (xn) in x becomes a float
		brightness = [float(yn) for yn in brightness] #every element (yn) in y becomes a float
		magnitude = np.array(magnitude) #transform your data in a numpy array, 
		brightness = np.array(brightness) #so the curve_fit can work
		
		popt, pcov = curve_fit(self.func, magnitude, brightness)
		plt.plot(magnitude, self.func(magnitude, *popt), 'r-', label="Steven's Power Curve")
		
		plt.legend(loc='upper left')
		print "a-value: ", popt[1]
		print "error: ", pcov
		self.postjson(popt[1], pcov) #post json before showing plot
		plt.show()
	
	#generates expected y values for actuator used to plot Steven's power curve
	def y_predicted(self, magnitude):
		y_predicted = [0.5, 1, 1.5, 2, 2.5, 3]
		return y_predicted

	def fit_model(self, magnitude, brightness, steven_power_law):
		popt, pcov = curve_fit(self.func, magnitude, y_predicted)
		return popt

	def func(self, x, a, b):
		return x**a + b

	def postjson(self, avalue, error):
		data = {}
		data['a-value'] = avalue
		data['error'] = error.tolist() #prevents type error
		json_data = json.dumps(data)

		# write to file
		participant = 'Participant'
		participant += str(self.participantName)
		participantFolder = self.actuator + '/' + participant + '/'
		fileName = os.path.join(participantFolder, 'data.txt')         
		with open(fileName, 'w') as outfile:
		    json.dump(data, outfile)

		# url = "http://localhost:8080"
		# r = requests.post(url, data=jsonText)

class JNDTestCases(unittest.TestCase):

    def test_init(self):
        """Is init method working setting up properly?"""
        experiment = Experiment()
        # self.assertTrue(experiment.participantNumber == 1) # participant 1
        self.assertTrue(len(experiment.values) == 1001) #values has [0, 1000]
        self.assertTrue(len(experiment.ranges) == 0) # ranges is empty
        self.assertTrue(experiment.query in experiment.values) # a random number from self.values is set as query

    def test_actuator_and_nextrange(self):
    	experiment = Experiment()
    	old_query = experiment.query
    	self.assertTrue(len(experiment.actuators) != 0)
    	experiment.actuator_setup() # test if case of actuator_setup()
    	self.assertTrue(experiment.actuator in experiment.actuators) # assigned an actuator
    	self.assertTrue(experiment.query != old_query) # new query assigned in next_range()

    def test_change_value(self):
    	experiment = Experiment()
    	add_value = subtract_value = experiment.query
    	self.assertTrue(experiment.change_value(add_value, 100) == (experiment.query + 100)) # test addition
    	self.assertTrue(experiment.change_value(subtract_value, -100) == (experiment.query - 100)) # test subtraction

    def test_setters_and_getters(self):
    	experiment = Experiment()
    	# tests if getters return right value
    	experiment.set_lower_limit(0)
    	self.assertTrue(experiment.get_lower_limit() == 0)
    	experiment.set_upper_limit(1000)
    	self.assertTrue(experiment.get_upper_limit() == 1000)
    	self.assertTrue(experiment.get_query() == experiment.query)

    def test_remove_jnd_range(self):
    	experiment = Experiment()

    	experiment.query = 500
    	experiment.set_lower_limit(0)
    	experiment.set_upper_limit(1000)
    	experiment.remove_jnd_range() #should remove range [250, 750]
    	self.assertTrue(len(experiment.values) == 500) # fifty() and update_values() are removing 50% of range
    	self.assertTrue(len(experiment.ranges) == 1) #jnd range added

    	# check for overlapping removal
    	experiment.query = 200
    	experiment.set_lower_limit(0)
    	experiment.set_upper_limit(400)
    	experiment.remove_jnd_range() #should remove range [100, 300]
    	self.assertTrue(len(experiment.values) == 350)
    	self.assertTrue(len(experiment.ranges) == 2) #jnd range added

    def test_new_actuator(self):
    	#tests when values is empty and a new actuator needs to be used
    	experiment = Experiment()
    	experiment.actuator_setup()
    	experiment.values = []
    	experiment.next_range() # should print "Current actuator complete"

    def test_experiment_complete(self):
    	#tests when actuators are empty if the experiment ends
    	experiment = Experiment()
    	experiment.actuators = []
    	experiment.actuator_setup() #should print "Experiment complete!"

    def test_visualize(self):
    	experiment = Experiment()
    	experiment.actuator_setup()
    	experiment.values = [[400, [301, 589]], [200, [121, 300]], [40, [0, 79]], [690, [590, 800]], [100, [80, 120]], [900, [801, 1000]]]
    	experiment.visualize()

if __name__ == '__main__':
    unittest.main()