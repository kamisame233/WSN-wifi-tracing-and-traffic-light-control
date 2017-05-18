#!/usr/bin/env python
# -*- coding: utf-8 -*-

# seach geo location from wifi mac address
# 2016-06-20 K.OHWADA
import uuid
from selenium import webdriver
import sys
import urllib
import urllib2
import json
import time
import socket
import send_And_receive
import Find_my_ip
KEY = "AIzaSyCaiAbXW6ZBa1HCtZSiiSopemJBvd3utLE"
CMD_CHROMEDRIVER = "./chromedriver"

#
# GeoWifi
#
class GeoWifi():

	HEADERS = { 'Content-Type' : 'application/json' }

	def request(self, key, addr1, addr2 ):
		url = "https://www.googleapis.com/geolocation/v1/geolocate?key=" + key
		text = self.buildJson( addr1, addr2 )
#		print text
		req = urllib2.Request(url, text, self.HEADERS)
		res = urllib2.urlopen(req)
		body = res.read()
#		print body
		return self.parseResponse(body)

	def buildJson(self, addr1, addr2):
		obj = {}
		obj[ "wifiAccessPoints" ] = self.buildAddressList(addr1, addr2)
		text = json.dumps(obj)
		return text
	
	def buildAddressList(self, addr1, addr2):
		list = []
		list.append( self.buildAddress(addr1) )
		list.append( self.buildAddress(addr2) )
		return list

	def buildAddress(self, addr):
		dict = { "macAddress": addr }
		return dict

	def parseResponse(self, res):
		obj = json.loads(res)
		if obj["location"] is None:        
			print res
			return None
		if obj["location"]["lat"] is None:   
			print res
			return None
		if obj["location"]["lng"] is None:   
			print res
			return None
		if obj["accuracy"] is None: 
			accuracy = 0  
		else:
			accuracy = obj["accuracy"]  	
		ret = {}	
		ret["lat"] = obj["location"]["lat"]
		ret["lng"] = obj["location"]["lng"]		
		ret["accuracy"] = accuracy	
		return ret

# class end

def openChrome(lat, lng):
	#url = "https://maps.google.co.jp/maps?q=" + str(lat) + "," + str(lng) + "&z=12"
	url = "https://maps.google.com/maps?q=" + str(lat) + "," + str(lng) + "&z=12"
	#url ="http://maps.google.com/maps/api/staticmap?autoscale=1&size=640x640&maptype=roadmap&visual_refresh=true&markers=color:red|label:A|"+ str(lat) + "," + str(lng)  +"&markers=color:red|label:B|"+str(lat+0.01) + "," + str(lng+0.01)+"&markers=color:red|label:C|"+str(lat+0.02) + "," + str(lng+0.02)




#http://maps.google.com/maps/api/staticmap?center=Brooklyn+Bridge,New+York,NY&zoom=14&size=512x512&maptype=roadmap&markers=color:blue|label:S|40.702147,-74.015794&markers=color:green|label:G|40.711614,-74.012318&markers=color:red|color:red|label:C|40.718217,-73.998284&sensor=false
	driver = webdriver.Chrome( CMD_CHROMEDRIVER )
	driver.get(url);


def send(lat, lng,car_type):


	address=(Find_my_ip.find(),2333)
	send_And_receive.send(str(lat),address)
	time.sleep(0.3)
	send_And_receive.send(str(lng),address)
	time.sleep(0.3)
	send_And_receive.send(str(car_type),address)
	time.sleep(0.3)
	send_And_receive.send(str(Find_my_ip.find()),address)

'''
	#HOST = '192.168.182.137'     # The remote host
	HOST = Find_my_ip.find()
	PORT = 50007              # The same port as used by the server
	s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	s1.connect((HOST, PORT))
	s1.sendall(str(lat))

	s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	s2.connect((HOST, PORT))
	s2.sendall(str(lng))

	s3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	s3.connect((HOST, PORT))
	s3.sendall(str(car_type))
	s4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s4.connect((HOST, PORT))
	s4.sendall(str(Find_my_ip.find()))
	s1.close
	s2.close
	s3.close
	s4.close;
'''

# main

#args = sys.argv
#argc = len(args)
#if (len(args) < 3):
#	print 'Usage: python %s mac_addr_1 mac_addr_2' % args[0]
#	exit()

geo = GeoWifi()

mac1= ':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0,8*6,8)][::-1])
#print mac1

#res = geo.request( KEY, args[1], args[2] )
res = geo.request( KEY, mac1, mac1)

if res is None:
	exit()

print str(res["lat"]) + " " + str(res["lng"]) + " "+ str(res["accuracy"])
#openChrome( res["lat"], res["lng"] )

send( res["lat"], res["lng"],'normal')

while 1:
	send_And_receive.receive_normal()

print "Press CTRL+C to quit"
try:
	# endless loop
	while True:
		time.sleep(1)
except KeyboardInterrupt:
	# exit the loop, if key interrupt
	pass

# end		
