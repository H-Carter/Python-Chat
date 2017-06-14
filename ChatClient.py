import sys
import getopt
import socket

from receiver import Receiver
from sender import Sender

def usage(err):
	print("usage: python ChatClient.py -l <listening port number> -p <server address>")
	print(" ==> " + str(err))
	print("Terminating...")

def getOpts():
	try:
		opts, args = getopt.getopt(sys.argv[1:], 'l:p:')
	except getopt.GetoptError as err:
		usage(err)
		sys.exit()
	if args:
		usage("argument " + str(args) + " not recognized")
		sys.exit()
	if len(opts) < 2:
		usage("all options are required")
		sys.exit()
	return opts
	
def startMessage(listenPort, serverPort, serverAddr):
	print("\nSTARTING CHAT CLIENT")
	print(" - Listing Port Number: " + str(listenPort))
	print(" - Server Port Number: " + str(serverPort))
	print(" - Server Address: " + str(serverAddr))
	
def socketDetails(sock):
	print("\nCONNECTION MADE")
	print(" - sock: " + str(sock))
	
def setup(server, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		sock.connect((server, int(port)))
	except ConnectionRefusedError:
		print("\nERROR: Could not connect to specified server. Please try again.\n")
		sys.exit()
	else:
		return sock
	
def sendMessage(sock):
	sender = Sender(sock)
	return sender
	
def receiveMessage(sock):
	receiver = Receiver(sock)
	return receiver
	
if __name__ == "__main__":
	# Store listening and server ports
	opts = getOpts()
	listenPort = opts[0][1]
	serverPort = opts[1][1]
	serverAddr = 'localhost'
	
	# Display Starting Message
	startMessage(listenPort, serverPort, serverAddr)
	
	# Setup Client Messenger Socket
	sock = setup(serverAddr, serverPort)
	#socketDetails(sock)
	
	# Start message receiver thread
	receiver = receiveMessage(sock)
	receiver.start()
	
	# Start message sender thread
	sender = sendMessage(sock)
	sender.start()
	
	# Wait for threads to terminate
	sender.join()
	receiver.join()
		
	try:
		print("ATTEMPTING SHUTDOWN")
		sock.shutdown( socket.SHUT_WR )
		sock.close()
	except:
		pass
	
	print("\nTERMINATING PROGRAM")	
