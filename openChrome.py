
from selenium import webdriver
import sys
import urllib
import urllib2
import json
import time
import socket
KEY = "AIzaSyCaiAbXW6ZBa1HCtZSiiSopemJBvd3utLE"
CMD_CHROMEDRIVER = "./chromedriver"


def openChrome(lat, lng):
	#url = "https://maps.google.co.jp/maps?q=" + str(lat) + "," + str(lng) + "&z=12"
	#url = "https://maps.google.com/maps?q=" + str(lat) + "," + str(lng) + "&z=12"
	url ="http://maps.google.com/maps/api/staticmap?autoscale=1&size=640x640&maptype=roadmap&visual_refresh=true&markers=color:red|label:C|"+ str(lat) + "," + str(lng)  +"&markers=color:green|label:T|"+str(lat+0.01) + "," + str(lng+0.01)




#http://maps.google.com/maps/api/staticmap?center=Brooklyn+Bridge,New+York,NY&zoom=14&size=512x512&maptype=roadmap&markers=color:blue|label:S|40.702147,-74.015794&markers=color:green|label:G|40.711614,-74.012318&markers=color:red|color:red|label:C|40.718217,-73.998284&sensor=false
	driver = webdriver.Chrome( CMD_CHROMEDRIVER )
	driver.get(url);
