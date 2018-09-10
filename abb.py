import os
import requests
import classes

from requests.auth import HTTPBasicAuth
from classes import *

abbav_urlPrefix = "https://api.auroravision.net/"
urlTypes = {
	"authentication": "api/rest/authenticate",
	"getPlantInformation": "api/rest/v1/plant/%s/info"
}

def validateResponse(response):
	# parse token
	if response:
		return True	
	else:
		return False

"""
return X-AuroraVision-Token
"""
def getApiToken(name, pwd, apiKey):
	subURL = urlTypes["authentication"]
	url = abbav_urlPrefix + subURL

	# authentication
	basicAuth = HTTPBasicAuth(name, pwd)

	# header
	headers = {"X-AuroraVision-ApiKey": apiKey}

	# GET, return response
	response = requests.get(url, auth=basicAuth, headers=headers)

	# parse token
	if(validateResponse(response)):
		return response.json()["result"]
	else:
		return None


def getEntity():
	return "16140068"


def getPlantInformation(apiToken, entityID):
	url = abbav_urlPrefix + urlTypes["getPlantInformation"] % (entityID)

	# header
	headers = {"X-AuroraVision-Token": apiToken}

	# GET, return response
	response = requests.get(url, headers=headers)

	# parse token
	if(validateResponse(response)):
		return response.json()["result"]
	else:
		return None


	return url


if __name__ == '__main__':

	# abb authentication
	name = os.environ.get('ABBAV_Username')
	pwd = os.environ.get('ABBAV_Password')
	apiKey = os.environ.get('ABBAV_ApiKey')

	apiToken = getApiToken(name, pwd, apiKey)
	# print(apiToken)

	# get entity
	entityID = getEntity()

	# get plantInfo
	plantInfo = PlantInformation(
		getPlantInformation(apiToken, entityID)
	)
	print(plantInfo.plantName)

	# make singleton for each api type
	
	# write to firebase