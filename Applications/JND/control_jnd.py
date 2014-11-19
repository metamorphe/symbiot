import threading
import getch
import jnd_arduino as jnd

class KeyEventThread(threading.Thread):
	def __init__(self, ard):
		super(KeyEventThread, self).__init__()
		self.controller = ard
		self.value = 1000;

	def run(self):
		while True:
			z = getch.getch()
			# escape key to exit
			if ord(z) == ord('o'):
				print "Opened serial connection:"
				self.controller.open();

			if ord(z) == ord('f'):
				self.value = self.value + 5
				self.value = 1000 if self.value > 1000 else self.value
				print "Actuating to", self.value
				self.controller.actuate(6, self.value);
			if ord(z) == ord('d'):
				self.value = self.value + 1
				self.value = 1000 if self.value > 1000 else self.value
				print "Actuating to", self.value
				self.controller.actuate(6, self.value);
			if ord(z) == ord('s'):
				self.value = self.value - 1
				self.value = 0 if self.value < 0 else self.value
				print "Actuating to", self.value
				self.controller.actuate(6, self.value);
			if ord(z) == ord('a'):
				self.value = self.value - 5
				self.value = 0 if self.value < 0 else self.value
				print "Actuating to", self.value
				self.controller.actuate(6, self.value);
			if ord(z) == ord('c'):
				print "Closed serial connection"
				self.controller.close();
			if ord(z) == ord('q'):
				break

ard = jnd.JNDArduino();
ard.close();

kethread = KeyEventThread(ard)
kethread.start()