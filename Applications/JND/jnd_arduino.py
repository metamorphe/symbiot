## import the serial library
import serial

class JNDArduino:
	def __init__(self):
		
		## Boolean variable that will represent 
		## whether or not the arduino is connected
		self.connected = False

		## open the serial port that your ardiono 
		## is connected to.
		
		self.ser = serial.Serial("/dev/tty.usbmodem1451", 9600)


	def open(self):
		## loop until the arduino tells us it is ready
		# while not self.connected:
		# 	serin = self.ser.read()
		# 	print serin
		# 	connected = True
		self.ser.open()

			
	""" 
		Actuates an actuator at address with value[0, 100]
		Ex. actuate(1, 100) => Turn on LED at location 1
	"""
	def actuate(self, address, value):
		## Tell the arduino to blink!
		self.ser.write("1")

		## Wait until the arduino tells us it 
		## is finished blinking
		while self.ser.read() == "1":
		    self.ser.read()

	def close(self):
		self.ser.close()


