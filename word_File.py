#! /usr/bin/python3

import requests,gi.repository
from bs4 import BeautifulSoup
gi.require_version('Notify','0.7')
from gi.repository import Notify,GdkPixbuf
import pyttsx3

res = requests.get('http://www.merriam-webster.com/word-of-the-day')
bs_Obj = BeautifulSoup(res.text,'lxml')

#Finding the word of the day
word_of_the_day = bs_Obj.h1.get_text()

#About the Word 
word_type = bs_Obj.find('span',{'class':'main-attr'}).get_text()

#Finding the meaning of the word or single meaning and examples:
try:
    meaning = bs_Obj.find('div',{'class':'wod-definition-container'}).select('p')[0].get_text()+'\n'+bs_Obj.find('div',{'class':'wod-definition-container'}).select('p')[1].get_text()
#In case only a single meaning given and no examples too:
except IndexError:
    meaning = bs_Obj.find('div',{'class':'wod-definition-container'}).select('p')[0].get_text()
        
#Notification
Notify.init('Word_of_the_day')
nf = Notify.Notification.new(word_of_the_day.upper()+' ( '+word_type+' )',meaning)
image = GdkPixbuf.Pixbuf.new_from_file('./Desktop/Python Stuff/Scraping/MW_logo.png')
nf.set_image_from_pixbuf(image)
nf.show()

#Text to Speech
engine = pyttsx3.init()
engine.say(word_of_the_day)
engine.setProperty('rate',80)  #80 words per minute
engine.setProperty('volume',0.9) 
engine.runAndWait()
#Writing into a file

file = open('./Desktop/Python Stuff/Scraping/words_List.text','a')
file.write(word_of_the_day+':'+'\n'+meaning+'\n'+'\n')
file.close()
            
