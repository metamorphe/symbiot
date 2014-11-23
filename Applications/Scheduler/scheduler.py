#really what is happening is the scheduler is not being made different. 
#its turning commands into sparse representations

#quantizing on the fixed-time chunk is one way of avoiding splitting tasks
#each is a fixed time chunk. <actuation time = WCET> roughly equal for each actuator. 

# we know beforehand that tasks have a low WCET variance, however the commands change at run time, as a result of how objects are being scheduled.

#real-time scheduling

import requests
import jnd_arduino as jnd
import time, numpy as np



# base = "http://localhost:3000"
base = "http://expresso.cearto.com"

def api(url):
	print base + url
	resp = requests.get(base + url)
	return resp.json()

# get behavior from online repo
def get_actuator(id):
	url = "/api/actuators/" 
	return api(url)

def get_behavior(id):
	url = "/api/behaviors/" + str(id)
	return api(url)

def get_commands(id):
	url = "/api/behaviors/" + str(id) + "/sparse.json"
	return api(url)["sparse_commands"]


# send behavior
# ([[0, 254.9999999999999], [20, 0.0], [93, 255.0], [160, 0.0], [234, 255.0], [300, None]]
def send_behavior(id, ard, addr, velocity=6):
	commands = get_commands(id)
	# convert to differential time
	a = np.array(commands, dtype=np.float).T
	time_diff = np.convolve(a[0], [1, -1])[1:-1] # d/dt
	magnitudes = a[1][0:-1]
	norm = np.max(magnitudes)
	magnitudes = np.divide(magnitudes, norm)
	magnitudes = np.multiply(magnitudes, 100)

	diff_commands = np.array([time_diff, magnitudes])

	t0 = time.time()
	for t, v in diff_commands.T:
		# print "send", "t: %5.0f" % ((time.time() - t0) * 1000), "delay:%5.0f" % (t * velocity), "mag:%5.0f" % v
		ard.actuate(addr, 100 - v)
		time.sleep(t * velocity / 1000.) # delays for x ms
	
	# END BUFFER
	ard.actuate(addr, 0)
	time.sleep(0.5)



# MAIN EXECUTION LOOP
ard = jnd.JNDArduino();
ard.close();
ard.open();

transmission = 23
ekg = 8
raindrops = 18
lighthouse = 12

send_behavior(transmission, ard, 3, 6)
send_behavior(lighthouse, ard, 6, 6)
send_behavior(ekg, ard, 5, 6)
ard.close();
# send behavior multiplexing
