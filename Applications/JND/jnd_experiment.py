import random, os

class Experiment:
	
	participantNumber = 0

	def __init__(self):
		# self.participant = participantNumber
		# Experiment.participantNumber += 1 #change participant counter
		self.actuators = ["LED", "heatpad"]
		print "Press 'r' to start the first actuator" #runs actuator_setup


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
			print "Actuating to ", self.query



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
			self.ranges.append([self.query, self.jnd_range])
			self.values = self.update_values()
			print "Range added"

	def update_values(self):
		print "Pre: ", self.values
		down, up = self.fifty()
		#Cesar - this range isn't being removed
		print "Range that should be removed ", up, down
		up += 1 #correcting limits
		for j in range(down, up):
			#index of the candidate value
			try:
				self.values.remove(j)
			except ValueError:
				pass
		print "Post: ", self.values
		return self.values


	def fifty(self):
		down = self.jnd_range[0]
		up = self.jnd_range[1]
		fifty_up = (self.query - up) / 2
		fifty_up += self.query
		print "fifty up ", fifty_up
		fifty_down = (self.query - down) / 2
		fifty_down += self.query
		print "fifty down ", fifty_down
		fifty_range = [fifty_down, fifty_up]
		return fifty_range


