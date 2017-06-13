import threading
import connections
import sys

class Relay( threading.Thread ):

	def __init__(self, socket, addr):
		threading.Thread.__init__(self)
		self.socket = socket
		self.addr = addr
			
	def run(self):
		while True:
			try:
				msg_bytes = self.socket.recv(1024)
			except:
				break
			if len(msg_bytes):
				message = str(self.addr) + ": " + msg_bytes.decode()
				print(message)
			else:
				print("No bytes received.")
				self.socket.close()
				connections.sockets.remove(self.socket)
				if not connections.sockets:
					print("No more connections - exiting")
					sys.exit()
				break
				
			for socket in connections.sockets:
				if socket is not self.socket:
					socket.send(message.encode())