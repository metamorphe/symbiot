import serial, sys, glob, time

# Opens a serial connection to an Arduino

class JNDArduino:
	def __init__(self):
		avail_ports = serial_ports()
		if(len(avail_ports) == 0):
			raise EnvironmentError("No ports detected. Plug in the Arduino! >:(");

		self.ser = serial.Serial(avail_ports[0], 9600)
		self.connected = self.ser._isOpen
		# Make sure its closed
		self.close()
	""" 
		Actuates an actuator at address with value[0, 1000]
		Ex. actuate(1, 1000) => Turn on LED at location 1
	"""
	def actuate(self, address, value):	
		value = int(value)
		self.ser.write(str(address))
		self.ser.write(",")
		self.ser.write(str(value))
		self.ser.write("\n")


	def open(self):
		self.ser.open()
		self.ser.flush()
		print "Starting up Arduino ..."
		time.sleep(1) # give the Arduino time to start up

	def flush(self):
		self.ser.flush();

	def close(self):
		print "Shutting down Arduino ..."
		time.sleep(1)  # let it finish what its doing. 
		self.ser.close()


def serial_ports():
	"""Lists serial ports

	:raises EnvironmentError:
		On unsupported or unknown platforms
	:returns:
		A list of available serial ports
	"""
	if sys.platform.startswith('win'):
		ports = ['COM' + str(i + 1) for i in range(256)]

	elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
		# this is to exclude your current terminal "/dev/tty"
		ports = glob.glob('/dev/tty.usb[A-Za-z]*')

	elif sys.platform.startswith('darwin'):
		ports = glob.glob('/dev/tty.usb*')

	else:
		raise EnvironmentError('Unsupported platform')

	result = []
	for port in ports:
		try:
			s = serial.Serial(port)
			s.close()
			result.append(port)
		except (OSError, serial.SerialException):
			pass
	return result


