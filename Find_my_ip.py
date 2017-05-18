import socket
import send_And_receive
import time

def find():
#find my ip
	x = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	x.connect(('8.8.8.8', 1))  # connect() for UDP doesn't send packets
	local_ip_address = x.getsockname()[0]
	return local_ip_address
