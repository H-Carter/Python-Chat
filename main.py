import options
import server, client

def show(type, portNum, serverAddre):
	print("\nSTARTING MESSENGER " + str(type))
	print(" - Port Number: " + str(portNum))
	print(" - Server Address: " + str(serverAddr))


if __name__ == "__main__":
	# Read/verify command line options and arguments
	opts, args = options.getOptsArgs()
	# Store port number/server address
	portNum = args[0]
	serverAddr = 'localhost'
	if (len(args) == 2):
		serverAddr = args[1]
	
	# Determine Server or Client
	if opts:
		# Setup Server
		show("SERVER", portNum, serverAddr)
		sock, addr = server.setup(serverAddr, portNum)
		server.getDetails(sock, addr)
		
		# Start message receiver thread
		receiver = server.receiveMessage(sock)
		receiver.start()
		
		# Start message sender thread
		sender = server.sendMessage(sock)
		sender.start()
		
		# Wait for threads to terminate
		sender.join()
		receiver.join()
		
	else:
		# Setup Client
		show("CLIENT", portNum, serverAddr)
		sock = client.setup(serverAddr, portNum)
		client.getDetails(sock)
		
		# Start message receiver thread
		receiver = client.receiveMessage(sock)
		receiver.start()
		
		# Start message sender thread
		sender = client.sendMessage(sock)
		sender.start()
		
		# Wait for threads to terminate
		sender.join()
		receiver.join()
		
	try:
		print("Attempting socket shutdown.")
		sock.shutdown( socket.SHUT_WR )
		sock.close()
	except:
		pass
	
	print("\n***THE END***\n")	
		
