#Handles http requests
import requests

#To convert r.text into dictionary format
import json

#To convert text into speech
import pyttsx3

print('Welcome to Mr. Weather Reporter, developed by Vipashana Shahakar.')
city=input('Enter a city: ')

#inserting API and city
url=f'https://api.weatherapi.com/v1/current.json?key=48c10338fd5844b6b8854854241706&q={city}'

#calling requests method on url
r=requests.get(url)
#print(r.text)

#converting r.text into dictionary
weather_dict=json.loads(r.text)
temp=weather_dict['current']['temp_c']
atmosphere=weather_dict['current']['condition']['text']
humidity=weather_dict['current']['humidity']
feels=weather_dict['current']['feelslike_c']
#print(feels)
#print(humidity)
#print(atmosphere)

#Adding speech engine
engine = pyttsx3.init()
rate = engine.getProperty('rate')

#Controls the speed of speaking
engine.setProperty('rate', rate + 10)


#Tells current temperature and feels like
engine.say(f'Current temperature in {city} is {temp} celcius which feels like {feels} celcius')

#Tells current atmosphere
engine.say((f'It is {atmosphere} outside'))

#Tells humidity
engine.say(f'Humidity in air is {humidity} celcius. Have an amazing day!')

engine.runAndWait()