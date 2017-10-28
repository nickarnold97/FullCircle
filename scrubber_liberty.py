import requests
import json

latitude = 0
longitude = 0

flag = True

def entervariables(lat,lon):
	#print(lat)
	#print(lon)
	latitude = 0
	longitude = 0
	latitude += (lat)
	longitude += (lon)
	return latitude, longitude

while flag:
	latitude, longitude = entervariables(42.3495073,-71.1070262)
	#print(latitude)
	#print(longitude)

	url = "https://apis.solarialabs.com/shine/v1/total-home-scores/reports?lat=%f&lon=%f&apikey=2IZ6qYkVCwEERUa0EjC00SGFVIQNBlJM" % (latitude, longitude)
	#print(url)
	#response = requests.get("https://apis.solarialabs.com/shine/v1/total-home-scores/reports?street-number=700&street-name=Commonwealth Ave.&city=Boston&state=MA&zip-code=02215&lat=42.3495073&lon={-71.1070262}&apikey=2IZ6qYkVCwEERUa0EjC00SGFVIQNBlJM")
	#response = requests.get("https://apis.solarialabs.com/shine/v1/total-home-scores/reports?lat=42.3495073&lon=-71.1070262&apikey=2IZ6qYkVCwEERUa0EjC00SGFVIQNBlJM")
	response = requests.get(url)
	responseObj = json.loads(response._content)
	#print(responseObj)

	temp = (latitude, longitude)
	
	finaldict = {}

	finaldict[temp] = responseObj['totalHomeScores']['safety']['value']

	for key, value in finaldict.items():
		print(key, value)
	
	print(responseObj['totalHomeScores']['safety']['value'])

	flag = False


