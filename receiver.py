import threading
import os, sys

class Receiver( threading.Thread ):

	def __init__(self, socket):
		threading.Thread.__init__(self)
		self.socket = socket
			
	def run(self):
		while True:
			print("still in receiver loop")
			try:
				msg_bytes = self.socket.recv(1024)
			except:
				print("Receiving error. Exiting(sys.exit()) receiving thread.")
				sys.exit()
			if len(msg_bytes):
				print(" ==> " + msg_bytes.decode())
				msg_bytes = self.socket.recv(1024)
			else:
				print("No bytes received. Exiting(os._exit()) receiving thread.")
				self.client_socket.close()
				os._exit( 0 )