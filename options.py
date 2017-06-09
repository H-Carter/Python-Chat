import sys
import argparse
import getopt

def usage(err):
	print("usage: input_program.py [-o O] [-t T] [-h]")
	print("   --> " + str(err))
	print("\nTerminating...")

def getOpts():
	try:
		opts, args = getopt.getopt(sys.argv[1:], 'o:t:h')
	except getopt.GetoptError as err:
		usage(err)
		sys.exit()
	if (args):
		usage("invalid argument(s) " + str(args))
		sys.exit()
	return opts
		
def printOpts(opts):
	optDict = dict(opts)
	if '-o' in optDict:
		print("option 1: " + optDict['-o'])
	if '-t' in optDict:
		print("option 2: " + optDict['-t'])
	if '-h' in optDict:
		print("option 3")