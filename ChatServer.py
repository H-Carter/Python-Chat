import sys
import getopt
import socket

import connections

from relay import Relay

def usage(err):
	print("usage: python ChatServer.py <listening port number>")
	print(" ==> " + str(err))
	print("Terminating...")

def startMessage(listenPort, serverAddr):
	print("\nSTARTING CHAT SERVER")
	print(" - Listing Port Number: " + str(listenPort))
	print(" - Server Address: " + str(serverAddr))

def socketDetails(sock, addr):
	print("\nCONNECTION MADE")
	print(" - sock: " + str(sock))
	print(" - addr: " + str(addr))

def sendMessage(sock):
	sender = Sender(sock)
	return sender

def receiveMessage(sock):
	receiver = Receiver(sock)
	return receiver
	
if __name__ == "__main__":
	# Store port number/server address
	try:
		listenPort = sys.argv[1]
	except:
		usage("No listening port number entered.")
		sys.exit()
	serverAddr = 'localhost'
	startMessage(listenPort, serverAddr)
	
	# Setup Server
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	serversocket.bind((serverAddr, int(listenPort)))
	serversocket.listen(5)
	
	while True:
		# Accept new socket connection
		sock, addr= serversocket.accept()
		socketDetails(sock, addr)
		
		# Add new connection to connection list
		connections.sockets.append(sock)
		
		# Start new connection relay thread
		Relay(sock, addr).start()
	
	# Wait for thread to terminate
	receiver.join()

