import requests
from requests.exceptions import HTTPError
from zip_city_classes import *
import json

def welcomeStatement():
	print('''\tWelcome to Dads weather station application
	Where the weather comes first, then the mowing begins''')
	print()

def Options_0(options = ''):
		options = input('Do you want to see weather by city?: press 1 or zipcode press 2?: ')
		if options == '1':
			user_city = GeoCity('')
			user_city.city_1()
		elif options == '2':
			user_zip = GeoZip('')
			user_zip.zip_0()
		else:
			print('no')

checkAnother = 'yes'
while checkAnother == 'yes' or checkAnother == 'y':
	welcomeStatement()
	Options_0()

	print('Do you want to check another location? (yes or no)')
	checkAnother = input('yes/no: ')
	if checkAnother == 'yes':
		continue
	if checkAnother == "no":
		print("Thank you for choosing my weather application!")
	else:
		print('Please type yes or no')
		checkAnother = input('yes/no: ')
	continue
		
