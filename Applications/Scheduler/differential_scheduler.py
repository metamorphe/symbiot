
def d_dt(commands):
	a = np.array(commands, dtype=np.float).T
	time_diff = np.convolve(a[0], [1, -1])#[1:-1] # d/dt, remove extra element
	
	# END COMMANDS WITH MAG 0
	time_diff[-1] = 0
	time_diff = time_diff[1:]
	a[1][-1] = 0

	diff_commands = np.array([time_diff, a[1]])
	return diff_commands.T


def send_behavior(ard, addr, id,  velocity=1):
	print "SYNCHRONOUS SEND"
	commands = api.get_commands(id, velocity)
	# convert to differential time
	diff_commands = d_dt(commands)
	t0 = time.time()

	log = []

	for t, v in diff_commands:
		# print "send", "t: %5.0f" % ((time.time() - t0) * 1000), "delay:%5.0f" % (t * velocity), "mag:%5.0f" % v
		ard.actuate(addr, v)
		log.append(Job(id, time.time() - t0, v , addr));
		print "COMMAND @", "{:3.2f}".format(time.time() - t0), "to", "{:1.0f}".format(addr) + ":" + "{:3.0f}".format(v )
		time.sleep(t) # delays for x ms
	
	# END BUFFER
	ard.actuate(addr, 0)
	time.sleep(0.5)
	print "SYNCHRONOUS END"
	return log