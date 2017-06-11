import sys
import socket

from receiver import Receiver
from sender import Sender

def setup(server, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		sock.connect((server, int(port)))
	except ConnectionRefusedError:
		print("\nERROR: Could not connect to specified server. Please try again.\n")
		sys.exit()
	else:
		return sock
	
def getDetails(sock):
	print("\nCONNECTION MADE")
	#print("	- sock: " + str(sock))
	
def sendMessage(sock):
	sender = Sender(sock)
	return sender
	
def receiveMessage(sock):
	receiver = Receiver(sock)
	return receiver