# Code patched together with help from VirusTotal documentation
# This requires an API key - register a free account with VT for this
# Create a file called out.txt and store in same directory as this script
# Dump a list of MD5 hashes into a file called md5list.txt in same directory
# snoozesecurity.blogspot.com

import requests
import time

url = 'https://www.virustotal.com/vtapi/v2/file/report'

def writeResults(response):
	with open("out.txt", "a") as myfile:
		myfile.write(str(response.json()))
		myfile.write("\n")
		myfile.close()

with open("md5list.txt") as md5s:
	for line in md5s:
		params = {'apikey': 'your_api_key', 'resource': line}
		response = requests.get(url, params=params)
		writeResults(response)
		time.sleep(20)
