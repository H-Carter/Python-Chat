import threading
import connections
import sys, os

class Relay( threading.Thread ):

	def __init__(self, socket, addr, name):
		threading.Thread.__init__(self)
		self.socket = socket
		self.addr = addr
		self.name = name
			
	def run(self):
		while True:
			# Read bytes from socket
			try:
				msg_bytes = self.socket.recv(1024)
			except:
				print("SOCKET RECEIVING ERROR")
				connections.sockets.remove(self.socket)
				self.socket.close()
				sys.exit()

			# Check message
			if msg_bytes:
				message = msg_bytes.decode()
				if (message == "EXITING"):
					message = self.name + " HAS LEFT"
					print(message)
					for socket in connections.sockets:
							if socket is not self.socket:
								socket.send(message.encode())
					connections.sockets.remove(self.socket)
					self.socket.close()
					# Check if any connections 
					if not connections.sockets:
						print("ALL CLIENTS HAVE DISCONNECTED")
					sys.exit()
				else:
					message = self.name + ": " + message
					print(message)

				# Relay message to all other connected clients
				for socket in connections.sockets:
					if socket is not self.socket:
						socket.send(message.encode())
				
			else:
				print("NO BYTES RECEIVED")
				connections.sockets.remove(self.socket)
				self.socket.close()
				if not connections.sockets:
					print("ALL CLIENTS HAVE DISCONNECTED")
				sys.exit()

