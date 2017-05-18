# Echo server program
import socket
import send_And_receive
import Find_my_ip
def LightControl():

	print 'traffic light changed';






#HOST = '127.0.0.1'                 # Symbolic name meaning all available interfaces
#HOST = ''  
#HOST = '192.168.182.137' 
#PORT = 8080             # Arbitrary non-privileged port
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s.bind((HOST,PORT))
#s.listen(5)

while 1:
	#conn, addr = s.accept()
	#print 'Connected by', addr
	#data = conn.recv(1024)
	#print 'Received instruction', data

	data1=send_And_receive.receive()
	#print 'Traffic light ip :'+Find_my_ip.find()
	#print 'Received instruction data1 ', data1
	LightControl()

	#conn.sendall(data)
	#send IP as echo data
	#conn.sendall(local_ip_address)
	#if data=="kami": break
	#if not data: break
	
conn.close()
