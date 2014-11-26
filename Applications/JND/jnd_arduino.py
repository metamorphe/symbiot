import serial, sys, glob

class JNDArduino:
	def __init__(self):
		avail_ports = serial_ports()
		if(len(avail_ports) == 0):
			raise EnvironmentError("No ports detected. Plug in the Arduino! >:(");

		self.ser = serial.Serial(avail_ports[0], 9600)
		self.connected = self.ser._isOpen
		# Make sure its closed
		self.close()

	def open(self):
		self.ser.open()

	def flush(self):
		self.ser.flush();
	""" 
		Actuates an actuator at address with value[0, 1000]
		Ex. actuate(1, 1000) => Turn on LED at location 1
	"""
	def actuate(self, address, value):	
		self.ser.write(str(address))
		self.ser.write(",")
		self.ser.write(str(value))
		self.ser.write("\n")


	def close(self):
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


