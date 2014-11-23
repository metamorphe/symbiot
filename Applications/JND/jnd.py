import os, sys, time, datetime, json, random, operator
from operator import itemgetter

#Create specified actuator folder and specified participant folder
def newActuator(actuatorName, participantNumber):
	if not os.path.exists(actuatorName):
		print('Creating new folder for ' + actuatorName + '...')
		os.makedirs(actuatorName) # make folder for actuator
	print('Creating participant folder...') # create participant subfolder within actuator folder, CSV
#	experiments = [["light", "dark"]]
	participant = 'Participant'
	participant += str(participantNumber)
	participantFolder = actuatorName + '/' + participant + '/'
	os.makedirs(participantFolder)
	runExperiment(actuatorName, item)

# #GOES IN CREATE JSON
# #Create JSON for specified actuator and specified participant
# def runExperiment(actuatorName, participantNumber):
# 	print('Running ' + actuatorName + ' Experiment for Participant ' + participantNumber + ' ...')
# 	data = {}
# 	data['actuator'] = actuatorName
# 	data['participant'] = participantNumber
# 	data['startTime'] = str(datetime.datetime.now().strftime("%m/%d/%Y %H:%M"))
# 	# data['xValues'] = 
# 	# data['yValues'] = 
# 	#buttonpresses
# 	json_data = json.dumps(data)
# 	postJson(json_data)
# #post json to URL
# def postJson(json):
# 	url = "http://localhost:8080"
# 	r = requests.post(url, data=json)

# def actuate(intensity):
# 	#actuate at given intensity
# 	print("actuating")

# def run_experiment():
# 	ranges = []
# 	values = []
# 	# set of query points [0, 100]
# 	for i in range(0, 1001):
# 		values.append(i)
# 	query = random.choice(values)
# 	while not len(values) == 0:
# 		print "Pre: ", values
# 		jnd_range = jnd(query)
		
# 		print query, ": [", jnd_range, "]"
# 		# remove query and 50% range from index
# 		values = remove_range(values, jnd_range)
# 		ranges.append([query, jnd_range])
# 		if len(values) != 0:
# 			query = random.choice(values)
# 	sorted_ranges = sorted(ranges, key=itemgetter(0))


# def remove_range(values, jnd_range):
# 	down, up = jnd_range
# 	up = up + 1 # correcting limits
# 	for j in range(down, up):
# 		# index of the candidate value
# 		try:
# 			values.remove(j)
# 		except ValueError:
# 			pass
# 	print "Post: ", values
# 	return values
	

# def jnd(query):
# 	up = query + 5
# 	up = 100 if up > 100 else up
# 	down = query - 5
# 	down = 0 if down < 0 else down

# 	# while (!noticed):
# 	# 	up+=1
# 	# 	actuate(up)
# 	# noticed = false
# 	# while (!noticed):
# 	# 	down-=1
# 	# 	actuate(down)
# 	# wait for button press for up
# 	# wait for button press for down
# 	# return the full range
# 	jnd_range = [down, up]
# 	return jnd_range

# def fifty(up, down, comparison):
# 	fifty_up = (comparison - up)/2
# 	fifty_down = (comparison - down)/2
# 	return fifty_up, fifty_down

def find_threshold(point, alpha):
	# noticed = false #jnd noticed
	# up = down = point
	# while (!noticed):
	# 	up+=1
	# 	actuate(up)
	# noticed = false
	# while (!noticed):
	# 	down-=1
	# 	actuate(down)
	# return range(down, up)

	up_k = k_value(up, point)
	down_k = k_value(down, point)
	return [up_k, down_k]

def k_value(just_noticed, original):
	if just_noticed < original:
		return (just_noticed - original)/original
	else:
		return (original - just_noticed)/original


# remove_range([0, 1, 2, 3, 4], [3, 4]);
# [0, 1, 2]


# actuatorName = raw_input('Enter Actuator Name: ')
# participantNumber = raw_input('Participant Number: ')
# runExperiment(actuatorName, participantNumber)

# add command args
# -ls outputs all of the actuator names that we have on file
# -r "actuator name" "id"
# - participant