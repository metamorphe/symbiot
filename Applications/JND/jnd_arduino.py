import serial

class JNDArduino:
	def __init__(self):
		self.ser = serial.Serial("/dev/tty.usbmodem1411", 9600)
		self.connected = False

	def open(self):
		# print self.connected
		if not self.connected:
			self.ser.open()
			self.connected = True
			
	""" 
		Actuates an actuator at address with value[0, 1000]
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



