import threading
import os, sys

class Sender ( threading.Thread ):

	def __init__(self, socket):
		threading.Thread.__init__(self)
		self.socket = socket
		
	def run(self):
		while True:
			stringIn = sys.stdin.readline()
			if stringIn:
				self.socket.send(stringIn.encode())
			else:
				self.socket.send('EXITING'.encode())
				os._exit( 0 )