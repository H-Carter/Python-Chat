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
				print("Sending empty message to terminate sender thread and close socket")
				self.socket.send(''.encode())
				os._exit( 0 )