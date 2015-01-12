import threading
import getch
from jnd_experiment import Experiment
import jnd_arduino as jnd

class KeyEventThread(threading.Thread):
	def __init__(self):
		super(KeyEventThread, self).__init__()
		self.controller = ard
		self.experiment = Experiment()
		self.value = 1000;

	def run(self):
		open_connection = False
		while True:
			z = getch.getch()

			# if ord(z) == ord('w'):
			# 	self.controller.open();

			#Start experiment and/or trial
			if ord(z) == ord('['):
				if (open_connection == False):
					open_connection = True
					print "Opened serial connection:"
					self.controller.open();
				username = raw_input("Please enter your initials: ")
				self.experiment.actuator_setup(username)
				self.value = self.experiment.get_query()
				# print "new value ", self.value
				self.controller.actuate(5, self.value);
				self.controller.actuate(3, self.value);

			#Change actuated values
			if ord(z) == ord('h'):
				self.value = self.experiment.change_value(self.value, 10)
				self.controller.actuate(3, self.value);
			if ord(z) == ord('g'):
				self.value = self.experiment.change_value(self.value, 5)
				self.controller.actuate(3, self.value);
			if ord(z) == ord('f'):
				self.value = self.experiment.change_value(self.value, 1)
				self.controller.actuate(3, self.value);
			if ord(z) == ord('d'):
				self.value = self.experiment.change_value(self.value, -1)
				self.controller.actuate(3, self.value);
			if ord(z) == ord('s'):
				self.value = self.experiment.change_value(self.value, -5)
				self.controller.actuate(3, self.value);
			if ord(z) == ord('a'):
				self.value = self.experiment.change_value(self.value, -10)
				self.controller.actuate(3, self.value);


			#Set/Reset upper and lower limits
			if ord(z) == ord('k'):
				self.experiment.set_lower_limit(self.value)
				self.experiment.remove_jnd_range()
			if ord(z) == ord('l'):
				self.experiment.set_upper_limit(self.value)
				self.experiment.remove_jnd_range()

			if ord(z) == ord('i'):
				self.experiment.set_lower_limit(False) #reset
				print "reset lower limit"
			if ord(z) == ord('o'):
				self.experiment.set_upper_limit(False) #reset
				print "reset upper limit"


 			#find next range
			if ord(z) == 32: #spacebar
				self.value = self.experiment.next_range()
				if (self.value != False or self.value == 0): #not a new actuator
					print 'new value ', self.value
					self.controller.actuate(5, self.value);
					self.controller.actuate(3, self.value);


			if ord(z) == ord('c'):
				print "Closed serial connection"
				self.controller.actuate(5, 0)
				self.controller.actuate(3, 0);
				self.controller.close();
				break

			# if ord(z) == ord('q'):
			# 	break


ard = jnd.JNDArduino();

kethread = KeyEventThread()
kethread.start() #automatically start script