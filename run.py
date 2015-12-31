# This script will display the information about a perticular ip
# in command line

import requests
import sys
import json

arguments = sys.argv

def print_info(data):
	parsed_data = json.loads(data)
	
	for info in parsed_data:
		print info + ':' + ' ' + parsed_data[info]

def get_data(*arg):
	if len(arg) == 1:
		data = requests.get('http://ipinfo.io/'+ arg[0] +'/json').text
		print_info(data)
	else:
		data = requests.get('http://ipinfo.io/json').text
		print_info(data)

# means it has IP address
if len(arguments) > 1:
	ip = arguments[1]
	get_data(ip)
else:
	get_data()

