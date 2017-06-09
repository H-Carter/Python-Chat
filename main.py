import options
import input
import server, client

if __name__ == "__main__":

	# Read command line options and arguments
	# terminates if usage is incorrect
	opts, args = options.getOptsArgs()
	
	# Store port number/server address
	portNum = args[0]
	serverAddr = 'localhost'
	if (len(args) == 2):
		serverAddr = args[1]
	
	# Determine Server or Client
	if opts:
		print("\nMESSENGER SERVER")
		print("	- Port Number: " + str(portNum))
		print("	- Server Address: " + str(serverAddr))
		# Setup Server
		sock, addr = server.setup(serverAddr, portNum)
		# Display connection details
		# server.getDetails(sock, addr)
		# Input and display messages
		server.receive(sock)
		# Close socket
		server.end(sock)
	else:
		print("\nMESSENGER CLIENT")
		print("	- Port Number: " + str(portNum))
		print("	- Server Address: " + str(serverAddr))
		# Setup Client
		sock = client.setup(serverAddr, portNum)
		# Display connection details
		# client.getDetails(sock)
		# Send messages until standard input terminates
		client.sendMessage(sock)