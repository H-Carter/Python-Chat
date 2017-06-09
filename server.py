import sys
import socket

from receiver import Receiver

def setup(server, port):
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	#serversocket.bind((server, port))
	serversocket.bind(('', int(port)))
	serversocket.listen(5)
	sock, addr= serversocket.accept()
	return sock, addr
	
def getDetails(sock, addr):
	print("\nCONNECTION MADE")
	print("	- sock: " + str(sock))
	print("	- addr: " + str(addr))

# TODO: Replace with threaded receiver
def receiveMessage(sock):
	Receiver(sock).start()
	
def end(sock):
	print("CONNECTION TERMINATED: closing server.\n")
	sock.close()