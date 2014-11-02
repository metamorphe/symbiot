import os, sys, time, datetime, json

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

#Create JSON for specified actuator and specified participant
def runExperiment(actuatorName, participantNumber):
	print('Running ' + actuatorName + ' Experiment for Participant ' + participantNumber + ' ...')
	data = {}
	data['actuator'] = actuatorName
	data['participant'] = participantNumber
	data['startTime'] = str(datetime.datetime.now().strftime("%m/%d/%Y %H:%M"))
	# data['xValues'] = 
	# data['yValues'] = 
	#buttonpresses
	json_data = json.dumps(data)

#post json to URL
#def postJson(json):
	#url = "http://localhost:8080" #talk to Jasper about where to post, send Json text
	# r = requests.post(url, data=jsonText), headers=headers)

# def actuatorVis():
# 	visualization that plots data points of all participants for an actuator

# def participantVis():
# 	visualize for a particular participant for an actuator


actuatorName = raw_input('Enter Actuator Name: ')
participantNumber = raw_input('Participant Number: ')
runExperiment(actuatorName, participantNumber)

# add command args
# -ls outputs all of the actuator names that we have on file
# -r "actuator name" "id"
# - participant