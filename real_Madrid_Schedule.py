#! /usr/bin/python3

import requests,gi.repository
from bs4 import BeautifulSoup
gi.require_version('Notify','0.7')
from gi.repository import Notify,GdkPixbuf
import datetime
import twilio
from twilio.rest import TwilioRestClient

res = requests.get('http://realmadrid.com/en/football/schedule')
bs_Obj = BeautifulSoup(res.text,'lxml')

#Finding the timings of match

match_date = bs_Obj.time.get_text().split(sep='/')
match_time = bs_Obj.find('time',{'class':'m_highlighted_next_game_time'}).get_text()[:-2]

#Converting match timings to IST which is 3hrs 30 mins ahead of CEST
mft = datetime.datetime(int(match_date[0]),int(match_date[1]),int(match_date[2]),int(match_time.split(':')[0]),int(match_time.split(':')[1]))
mist = datetime.timedelta(hours=3,minutes=30)
final_match_date_and_time  = str(mist + mft)

#Teams and Competition info
competition = bs_Obj.p.findAll('span')[0].get_text()
teamA = bs_Obj.select('.m_highlighted_next_game_team')[0].strong.get_text()
teamB = bs_Obj.select('.m_highlighted_next_game_team')[1].strong.get_text()

#Notification
Notify.init('Match')
image = GdkPixbuf.Pixbuf.new_from_file('./Desktop/Python Stuff/Scraping/30046showing.png')
nf = Notify.Notification.new(competition,teamA+' vs '+teamB+'   '+final_match_date_and_time)
nf.set_image_from_pixbuf(image)
nf.show()
    
#Mobile Notification 
time_1 = mist+mft
time_2 = datetime.datetime.now()
if((time_1-time_2).days<=1):
    account_sid =  "ACf23e3efd69d2acab5a1d2ec0c74c1d8e"
    auth_token = "5de990cc293d7fed34811a4aac49d556"
    client = TwilioRestClient(account_sid, auth_token)     
    message = client.messages.create(body="Matchday :"+'\n'+competition+'\n'+teamA+' vs '+teamB+'\n'+'Kickoff on '+str(mist + mft),
    to="Replace with your phone number",
    from_="Replace with your Twilio number")
    print(message.sid)
