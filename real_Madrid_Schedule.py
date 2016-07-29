#! /usr/bin/python3

import requests,gi.repository
from bs4 import BeautifulSoup
gi.require_version('Notify','0.7')
from gi.repository import Notify,GdkPixbuf
import datetime
import twilio
from twilio.rest import TwilioRestClient

res = requests.get('http://realmadrid.com/en')
bs_Obj = BeautifulSoup(res.text,'lxml')

#Finding the timings of match

match_date = bs_Obj.time.get_text().strip().split(sep=' - ')[0].split(sep='-')
match_time = bs_Obj.time.get_text().strip().split(sep=' - ')[1]

#Converting match timings to IST which is 3hrs 30 mins ahead of CEST
mft = datetime.datetime(int(match_date[2]),int(match_date[1]),int(match_date[0]),int(match_time.split(':')[0]),int(match_time.split(':')[1]))
mist = datetime.timedelta(hours=3,minutes=30)
final_match_date_and_time  = str(mist + mft)

#Teams and Competition info
competition = bs_Obj.find('strong',{'itemprop':'superevent'}).get_text()
teamA = bs_Obj.select('span strong')[0].get_text().upper()
teamB = bs_Obj.select('span strong')[1].get_text().upper()

#Notification
if(competition != 'TRAINING SESSION'):
    Notify.init('Match')
    image = GdkPixbuf.Pixbuf.new_from_file('./Desktop/Python Stuff/Scraping/30046showing.png')
    nf = Notify.Notification.new(competition,teamA+' vs '+teamB+'   '+final_match_date_and_time)
    nf.set_image_from_pixbuf(image)
    nf.show()
    nf.close()
else:
    Notify.init('Match')
    image = GdkPixbuf.Pixbuf.new_from_file('./Desktop/Python Stuff/Scraping/30046showing.png')
    nf = Notify.Notification.new(competition,final_match_date_and_time)
    nf.set_image_from_pixbuf(image)
    nf.show()
    nf.close()
    
#Mobile Notification 
time_1 = mist+mft
time_2 = datetime.datetime.now()
if((time_1-time_2).days<=1):
    account_sid =  "Enter your sid"
    auth_token = "Enter your token"
    client = TwilioRestClient(account_sid, auth_token)     
    if(competition == 'TRAINING SESSION'):
        message = client.messages.create(body=competition+'\n'+final_match_date_and_time,
        to="Replace with your phone number"
        from_="Replace with your Twilio number"
        print(message.sid)
    else: 
        message = client.messages.create(body="Matchday :"+'\n'+competition+'\n'+teamA+' vs '+teamB+'\n'+'Kickoff on '+str(mist + mft),
        to="Replace with your phone number"
        from_="Replace with your Twilio number"
        print(message.sid)
