import threading
import os, sys

class Receiver( threading.Thread ):

	def __init__(self, socket):
		threading.Thread.__init__(self)
		self.socket = socket
			
	def run(self):
		while True:
			try:
				msg_bytes = self.socket.recv(1024)
			except:
				print("Receiving error. Exiting(sys.exit()) receiving thread.")
				sys.exit()
			message = msg_bytes.decode()
			if len(message):
				print(" ==> " + message)
			else:
				print("No bytes received. Exiting(os._exit()) receiving thread.")
				self.client_socket.close()
				os._exit( 0 )