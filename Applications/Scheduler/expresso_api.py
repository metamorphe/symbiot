
import requests, md5, json, requests_cache
import numpy as np
base = "http://localhost:3000"
password = "potatoes123"
# base = "http://expresso.cearto.com"

def get(url):
	print url
	resp = requests.get(base + url)
	return resp.json()

def post(url, payload):
	print base + url 
	m = md5.new()
	m.update(password)
	auth = 	m.hexdigest()
	# payload["auth"] = auth
	print payload

	headers = {'content-type': 'application/json'}
	resp = requests.post(base + url, data=json.dumps(payload), headers=headers)
	print resp.text
	# print resp.json()

# get behavior from online repo
def get_actuator(id):
	url = "/api/actuators/" 
	return get(url)

def get_behavior(id):
	url = "/api/behaviors/" + str(id)
	return get(url)

def get_commands(id, velocity = 1):
	url = "/api/behaviors/" + str(id) + "/sparse.json"
	commands = get(url)["sparse_commands"]
	a = np.array(commands, dtype=np.float).T

	base_velocity = 6 + velocity
	a[0] = a[0] * base_velocity / 1000.

	# NORMALIZING MAGNITUDES TO 0 - 1000
	norm = np.nanmax( a[1])
	a[1] =  a[1] / norm * 1000;

	return a.T

def send_behavior(name, wave):
	url = '/api/behaviors/scanner'
	data = {"behavior":{
				'name': name,
        		'states': wave
				}
			}
	post(url, data)
 
requests_cache.install_cache("api_cache")
# requests_cache.disabled()
