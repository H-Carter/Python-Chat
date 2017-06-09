import sys

def readingOld():
	print("Standard Input:")
	try:
		stringIn = input()
	except:
		return
	while stringIn:
		print("--> " + stringIn)
		try:
			stringIn = input()
		except:
			return
	print("Terminating...\n")
	
def echo():
	print("Standard Input:")
	stringIn = sys.stdin.readline()
	while stringIn:
		print(" ==> " + stringIn)
		stringIn = sys.stdin.readline()
	print("Terminating...\n")