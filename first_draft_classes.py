import requests
from requests.exceptions import HTTPError
import json
import time

class GeoZip:

	def __init__(self, zipcode):
		self.zipcode = zipcode

	def zip_0(self):
		while True:
			try:
				enterzip = int(input('zipcode: '))
			except ValueError:
				print('That is not a number')
			except HTTPError as http_err:
				print(f'HTTP error occured: {http_err}')
				break
			except Exception as err:
				print(f'Other error occurred: {err}')
				break

			else:
				if len(str(enterzip)) == 5:
					response = requests.get(f'https://api.openweathermap.org/geo/1.0/zip?zip={enterzip},us&appid=cacd50700b6d5c35a9001f8268bc70eb')
					response.raise_for_status()
					jsonResponse = response.json()
					jsonLon = jsonResponse['lon']
					jsonLat = jsonResponse['lat']

					response_0 = requests.get(f'https://api.openweathermap.org/data/2.5/onecall?lat={jsonLat}&lon={jsonLon}&exclude=minutely,hourly&appid=cacd50700b6d5c35a9001f8268bc70eb&units=imperial')
					response_0.raise_for_status()
					jsonResponse_0 = response_0.json()
					pretty_response = json.dumps(jsonResponse_0, indent=2)
					print(pretty_response)
					break
						

				else:
					print('Number needs to be five digits')
								
class GeoCity:
	
	def __init__(self, city_0):
		self.city_0 = city_0

	def city_1(self):
		while True:
			entercity = input('City: ')
			enterstate = input('State code (Arizona = az): ')
			confirm = input(f'Is this correct?, {entercity}, {enterstate}, yes or no: ')
			if confirm == 'yes':
				try:
					response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={entercity},{enterstate},us&limit=5&appid=cacd50700b6d5c35a9001f8268bc70eb')
					response.raise_for_status()
					jsonResponse = response.json()
					jsonLon = jsonResponse[0]['lon']
					jsonLat = jsonResponse[0]['lat']

					response_0 = requests.get(f'https://api.openweathermap.org/data/2.5/onecall?lat={jsonLat}&lon={jsonLon}&exclude=minutely,hourly&appid=cacd50700b6d5c35a9001f8268bc70eb&units=imperial')
					response_0.raise_for_status()
					jsonResponse_0 = response_0.json()
					pretty_response = json.dumps(jsonResponse_0, indent=2)
					print(pretty_response)
					break

				except HTTPError as http_err:
					print(f'HTTP error occured: {http_err}')
					break
				except Exception as err:
					print(f'Other error occurred: {err}')
					break

			elif confirm == 'no':
				print('Please try again')
					
