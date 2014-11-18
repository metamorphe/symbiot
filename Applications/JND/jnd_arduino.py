import serial

class JNDArduino:
	def __init__(self):
		self.ser = serial.Serial("/dev/tty.usbmodem1451", 9600)

	def open(self):
		self.ser.open()
			
	""" 
		Actuates an actuator at address with value[0, 100]
		Ex. actuate(1, 1000) => Turn on LED at location 1
	"""
	def actuate(self, address, value):
		self.ser.write(str(address))
		self.ser.write(",")
		self.ser.write(str(value))
		self.ser.write("\n")


	def close(self):
		self.ser.close()


