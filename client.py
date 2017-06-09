import sys
import socket
	
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
	print("	- sock: " + str(sock))
	
def sendMessage(sock):
	# Continuosly read from standard input
	print("\nBegin typing:\n")
	stringIn = sys.stdin.readline()
	while stringIn:
		print(" ==> " + stringIn)
		sock.send(stringIn.encode())
		stringIn = sys.stdin.readline()
	print("CONNECTION TERMINATED: closing client.\n")