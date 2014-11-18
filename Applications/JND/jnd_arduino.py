import serial
import threading
import getch


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
		


class JNDArduino:
	def __init__(self):
		self.ser = serial.Serial("/dev/tty.usbmodem1451", 9600)
		self.connected = False

	def open(self):
		# print self.connected
		if not self.connected:
			self.ser.open()
			self.connected = True
			
	""" 
		Actuates an actuator at address with value[0, 100]
		Ex. actuate(1, 1000) => Turn on LED at location 1
	"""
	def actuate(self, address, value):
		if self.connected:
			self.ser.write(str(address))
			self.ser.write(",")
			self.ser.write(str(value))
			self.ser.write("\n")


	def close(self):
		# if self.connected:
		self.ser.close()



ard = JNDArduino();
ard.close();

kethread = KeyEventThread(ard)
kethread.start()