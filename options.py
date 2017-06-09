import sys
import argparse
import getopt

def usage(err):
	print("usage: messenger.py [-l] <port number> [<server address>]")
	print(" ==> " + str(err))
	print("\nTerminating...")

def getOptsArgs():
	try:
		opts, args = getopt.getopt(sys.argv[1:], 'l')
	except getopt.GetoptError as err:
		usage(err)
		sys.exit()
	# Check if command line arguments were entered correctly	
	argc = len(args)
	if (argc < 1):
		usage("missing port number")
		sys.exit()
	if (argc > 2):
		usage("too many arguments")
		sys.exit()
	if '-l' in args:
		usage("'-l' must come BEFORE port number")
		sys.exit()
		
	return opts, args