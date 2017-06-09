import threading
import os, sys

class Receiver( threading.Thread ):

	def __init__(self, socket):
		threading.Thread.__init__(self)
		self.socket = socket
		
	def close():
		print("Other side has closed. Closing socket.")
		self.socket.close()
		os._exit( 0 )
		
	# def receiveMessage(socket):
		# while True:
			# try:
				# msg_bytes= socket.recv(1024)
			# except:
				# print("TERMINATING: Socket closed")
				# sys.exit()
			# if len(msg_bytes):
				# print("Client: " + msg_bytes.decode())
				# msg_bytes= socket.recv(1024)
			# else:
				# self.close(socket)
			

	def run(self):
		while True:
			try:
				msg_bytes = self.socket.recv(1024)
			except:
				print("TERMINATING: Socket closed")
				sys.exit()
			if len(msg_bytes):
				print("Client: " + msg_bytes.decode())
				msg_bytes = self.socket.recv(1024)
			else:
				self.close()