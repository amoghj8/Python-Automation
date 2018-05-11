#! /usr/bin/python3

import requests
import json
import sys
import gi
gi.require_version('Notify','0.7')
from gi.repository import Notify,GdkPixbuf
import pyttsx3

#Temperature of entered place
place = ''.join(sys.argv[1])
try:
    token = 'Enter your api key'
    url = 'http://api.openweathermap.org/data/2.5/weather?q='+place+'&APPID='+token
    res = requests.get(url)
    weatherData = json.loads(res.text)
    print('The temperature of '+place.capitalize()+ ' is : '+str(round((weatherData['main']['temp']-273.15),3))+' degrees')
    print('Humidity : '+str(weatherData['main']['humidity'])+'%')
    print('State : '+weatherData['weather'][0]['description'].capitalize())

except IndexError:
    print('\n'+'Its like this :'+'\n'+'\n'+' ./Desktop/Python\ Stuff/Scraping/weather.py add_desired_location_here'+'\n')
    token = 'Enter token here'

#Details of my current location
place = 'mysore'
url = 'http://api.openweathermap.org/data/2.5/weather?q='+place+'&APPID='+token
res = requests.get(url)
weatherData = json.loads(res.text)

#Notification
Notify.init('Weather')
ntf = Notify.Notification.new(place.capitalize(),'Temperature : '+str(round((weatherData['main']['temp']-273.15),3))+' degrees'+'\n'+'Humidity : '+str(weatherData['main']['humidity'])+'%'+'\n'+'State : '+weatherData['weather'][0]['description'].capitalize())
image = GdkPixbuf.Pixbuf.new_from_file('./Desktop/Python Stuff/Scraping/weather-icon.jpg')
ntf.set_image_from_pixbuf(image)
ntf.show()

#Text to Speech
engine = pyttsx3.init()
engine.say(place+' , '+' Temperature : '+str(round((weatherData['main']['temp']-273.15),3))+'degrees ,'+'\n'+'Humidity : '+str(weatherData['main']['humidity'])+'% ,'+'\n'+'State : '+weatherData['weather'][0]['description'])
engine.setProperty('rate',80)  #80 words per minute
engine.setProperty('volume',0.9) 
engine.runAndWait()


