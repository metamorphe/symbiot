	active = api.get_active_schedule(1, 3)["code"]
	print active 
	active_behavior = active["behavior_id"]

	# MAIN EXECUTION LOOP
	mc.master.open()
	# mc.master.actuate(actuators.green_led, 1000)
	# synchronous = send_behavior(mc.master, actuators.green_led, behaviors.easy, velocity)
	mc.master.close()

def send(ard, behavior, speed):
	commands = []
	for i in range(0, 10):
		commands.append((behavior, i))

	q = microbenchmark(commands, speed)
	base = []
	while not q.empty():
		base.append(q.get())
	scheduled = scheduled_send(ard, base)
	return calc_error(np.array(base), [np.array(scheduled)])

def all(ard, command):
	for i in range(0, 10):
		ard.actuate(i, command)
