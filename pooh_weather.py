import urllib.request
import json

def getWeather(task):
	f = urllib.request.urlopen(f'http://api.wunderground.com/api/df9e2877cf28fc84/geolookup/conditions/q/PA/{task}.json')
	json_string = f.read()
	parsed_json = json.loads(json_string)
	location = parsed_json['location']['city']
	temp_f = parsed_json['current_observation']['temp_f']
	print (f"Current temperature in {location} is: {temp_f}")
	f.close()

if __name__ == '__main__':
	getWeather('Pittsburgh')