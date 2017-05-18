# Echo server program
import openChrome
import socket
import send_And_receive
import time
import Find_my_ip



def sendInstruction(Instruction):
	#HOST1 = '134.76.63.1'    # The remote host
	HOST1 = '127.0.0.1'    # The remote host
	PORT1 = 8080              # The same port as used by the server
	#si = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	si = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	si.connect((HOST1, PORT1))
	si.sendall(str(Instruction))
	print 'sent Traffic light instruction:' + str(Instruction)
	#data = s.recv(1024)
	#print 'echo data:'+ data;
	si.close;

def sendInstruction1(Instruction):
	#address=('134.76.63.1' ,8080)
	#address=('10.10.8.1' ,8080)
	address=('127.0.0.1' ,8080)
	send_And_receive.send(Instruction,address);
	print 'sent Traffic light instruction:' + str(Instruction)
	

def trafficLightPlan(lat, lng, car_type,car_ip):
	Reference_lat=0
	Reference_lng=0
	normal='normal'
	#unnormal='unnormal'
	
	if car_type == normal:
		print 'sent traffic light signal back'
		#send back to car
		#address=('127.0.0.1' ,9090)
		address=(car_ip ,9090)
		Instruction='green light is on'
		time.sleep(1)
		send_And_receive.send(Instruction,address);

	else:
		Instruction='turn on x axis green light for special the car'
		#to traffic light
		#address=('127.0.0.1' ,8080)
		#address=('10.10.11.24' ,8080)
		address=(Find_my_ip.find() ,8080)
		
		time.sleep(1)
		send_And_receive.send(Instruction,address)
		print 'sent traffic light signal to traffic light';
		#sendInstruction1(Instruction)




'''
HOST =Find_my_ip.find()
#HOST = '127.0.0.1'                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
'''

while 1:
	'''
	conn, addr = s.accept()
	lat = conn.recv(1024)

	conn, addr = s.accept()
	lng = conn.recv(1024)

	conn, addr = s.accept()
	car_type = conn.recv(1024)

	conn, addr = s.accept()
	car_ip = conn.recv(1024)

	print 'Received lication:', str(lat)+''+str(lng) +' car type:'+ str(car_type)+'car ip:'+str(car_ip)
	'''
	lat=send_And_receive.receive_server()
	lng=send_And_receive.receive_server()
	car_type=send_And_receive.receive_server()
	car_ip=send_And_receive.receive_server()
	print 'Received location data:'+lat[0]+''+lng[0]+' Car type:'+car_type[0]+' Car ip:'+car_ip[0]

	openChrome.openChrome(float(lat[0]) ,float(lng[0]))
	trafficLightPlan(lat[0] ,lng[0],car_type[0],car_ip[0])

	
	
	#conn.sendall(data)
	#send IP as echo data
	#conn.sendall(local_ip_address)
	#if lon==0: break
	#if not data: break
	
conn.close()
