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
				try:
					self.socket.send(stringIn.encode())
				except:
					print("SOCKET SENDING ERROR - SHUTTING DOWN")
					os._exit(0)
			else:
				try:
					self.socket.send('EXITING'.encode())
				except:
					pass
				os._exit( 0 )