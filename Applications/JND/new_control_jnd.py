import threading
import getch
from jnd_experiment import Experiment
import jnd_arduino as jnd

class KeyEventThread(threading.Thread):
	def __init__(self):
		super(KeyEventThread, self).__init__()
		# self.controller = ard
		self.experiment = Experiment()
		self.value = 1000; #MAKE RANDOM

	def run(self):
		while True:
			z = getch.getch()
			# escape key to exit
			if ord(z) == ord('o'):
				print "Opened serial connection:"
				# self.controller.open();

			#Start actuator
			if ord(z) == ord('r'):
				self.experiment.actuator_setup()
				self.value = self.experiment.get_query()
				print "new value ", self.value
				# self.controller.actuate(6, self.value);

			#Change actuated values
			if ord(z) == ord('h'):
				self.value = self.experiment.change_value(self.value, 10)
				# self.controller.actuate(6, self.value);
			if ord(z) == ord('g'):
				self.value = self.experiment.change_value(self.value, 5)
				# self.controller.actuate(6, self.value);
			if ord(z) == ord('f'):
				self.value = self.experiment.change_value(self.value, 1)
				# self.controller.actuate(6, self.value);
			if ord(z) == ord('d'):
				self.value = self.experiment.change_value(self.value, -1)
				# self.controller.actuate(6, self.value);
			if ord(z) == ord('s'):
				self.value = self.experiment.change_value(self.value, -5)
				# self.controller.actuate(6, self.value);
			if ord(z) == ord('a'):
				self.value = self.experiment.change_value(self.value, -10)
				# self.controller.actuate(6, self.value);


			#Set/Reset upper and lower limits
			if ord(z) == ord('u'):
				self.experiment.set_lower_limit(self.value)
				self.experiment.remove_jnd_range()

			if ord(z) == ord('k'):
				self.experiment.set_lower_limit(self.experiment.query) #reset to query
				print "reset lower limit"
			#set upper limit
			if ord(z) == ord('i'):
				self.experiment.set_upper_limit(self.value)
				self.experiment.remove_jnd_range()
			if ord(z) == ord('l'):
				self.experiment.set_upper_limit(self.experiment.query) #reset to query
				print "reset upper limit"

 			#find next range
			if ord(z) == ord('n'):
				self.value = self.experiment.next_range()


			if ord(z) == ord('c'):
				print "Closed serial connection"
				# self.controller.close();
				json()
			if ord(z) == ord('q'):
				break



# ard = jnd.JNDArduino();
# ard.close();

kethread = KeyEventThread()
kethread.start() #automatically start script