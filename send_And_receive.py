import socket
import Find_my_ip

def send(message,address):

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.sendto(message, address)
	s.close;

def receive():
	s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	address1=(Find_my_ip.find(),8080)
	s1.bind(address1)
	data=s1.recvfrom(4096)
	s1.close
	print 'received data:'+str(data[0])
	return data;

def receive_normal():
	s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	address2=(Find_my_ip.find(),9090)
	s2.bind(address2)
	data=s2.recvfrom(4096)
	s2.close
	print 'received data:'+str(data[0])
	return data;

def receive_server():
	s3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	address3=(Find_my_ip.find(),2333)
	s3.bind(address3)
	data=s3.recvfrom(4096)
	s3.close
	#print 'received data:'+str(data)
	return data;

	
