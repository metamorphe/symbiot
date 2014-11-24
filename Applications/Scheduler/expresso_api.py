
import requests, md5, json, requests_cache
base = "http://localhost:3000"
password = "potatoes123"
# base = "http://expresso.cearto.com"

def get(url):
	print base + url
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

def get_commands(id):
	url = "/api/behaviors/" + str(id) + "/sparse.json"
	return get(url)["sparse_commands"]

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
