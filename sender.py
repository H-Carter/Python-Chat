import threading
import os, sys

class Sender ( threading.Thread ):

	def __init__(self, socket):
		threading.Thread.__init__(self)
		self.socket = socket
		
	def run(self):
		print("\nBegin Sending Messages:\n")
		while True:
			print("still in sender loop")
			stringIn = sys.stdin.readline()
			if stringIn:
				print("SENDING: " + stringIn)
				self.socket.send(stringIn.encode())
			else:
				print("Sending empty message to terminate sender thread and close socket")
				self.socket.send(''.encode())
				break