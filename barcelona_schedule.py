#! /usr/bin/python3

import requests
from bs4 import BeautifulSoup
import gi
gi.require_version('Notify','0.7')
from gi.repository import Notify
from gi.repository import GdkPixbuf
import datetime

res = requests.get('https://www.fcbarcelona.com')
bs_Obj = BeautifulSoup(res.text,'lxml')


#Match main competition 
mmc = bs_Obj.find('span',{'class':'match__main__competition'}).get_text().strip()

#Match main phase 
mmp = bs_Obj.find('span',{'class':'match__main__phase'}).get_text().strip()

#Match date and time data
match_time = bs_Obj.find('time',{'class':'match__main__date__data'}).get_text().split(' ')[2].strip()
match_date = bs_Obj.find('time',{'class':'match__main__date__data'}).get_text().strip().split(' ')[0].split('/')
mft = datetime.datetime(int(match_date[2]),int(match_date[1]),int(match_date[0]),int(match_time.split(':')[0]),int(match_time.split(':')[1]))

#Adjusting according to IST
mist = datetime.timedelta(hours=3,minutes=30)
final_match_date_and_time  = str(mist+mft)

#Teams 
teamA = bs_Obj.findAll('span',{'class':'scoreboard__team__name'})[0].get_text().strip()
teamB = bs_Obj.findAll('span',{'class':'scoreboard__team__name'})[1].get_text().strip()

#Notification
Notify.init('Match')
image = GdkPixbuf.Pixbuf.new_from_file('./Desktop/Python Stuff/Scraping/fc-barcelona-0v.jpg')
nf = Notify.Notification.new(mmc+' : '+mmp,teamA+' vs '+teamB+'   '+final_match_date_and_time)
nf.set_image_from_pixbuf(image)
nf.show()
nf.close()

