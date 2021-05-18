#!/usr/bin/python3

#Weather Reporter v1.0.1
#
#Author: Jacob Christensen
#
#Modified: 5/17/2021
#Non Working -- learing NOAA API

import requests, bs4, time, json

from requests.sessions import HTTPAdapter

noaa_link = 'https://forecast.weather.gov/MapClick.php?lat=39.51320670000007&lon=-104.75001159999994'
header = {'token':'nzvggsNfcZfmIBhruACmRCjIrhrgCHCh'}

""" Old HTTP functions 
def get_weather_current(link):

	weather = requests.get(link)
	weather_soup = bs4.BeautifulSoup(weather.text, 'html.parser')
	weather_summary = weather_soup.select('#current_conditions-summary > p')
	weather_detail = weather_soup.select('#current_conditions_detail td')
	forecast_detail = weather_soup.select('.forecast-text')

	return {
			'summary': weather_summary[0].getText().lstrip(), 
			'temp': weather_summary[1].getText(), 
			'humidity': weather_detail[1].getText(), 
			'wind': weather_detail[3].getText(),
			'forecast': forecast_detail[0].getText()
		}

def log_weather_http():

	while True:

		weather_report = get_weather_current(noaa_link)
		
		log_time = time.asctime() + ': '
		weather_log = open('weather.log', 'a')

		weather_log.write(log_time)

		for i in weather_report.values():

			if i == weather_report['forecast']:
				print(i)
				weather_log.write('"' + i + '"\n')
			else:
				print(i, end=', ')
				weather_log.write('"' + i + '", ')

		weather_log.close()
		
		time.sleep(3600)
"""

lat = '39.5186000'
lon = '-104.7613600'

def log_weather_api():
	begin_date = '2021-05-17'
	end_date = '2021-05-17'
	response = requests.get(f'https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=ZIP:80138&startdate={begin_date}&enddate={end_date}', headers=header)
	print(response.text)
log_weather_api()