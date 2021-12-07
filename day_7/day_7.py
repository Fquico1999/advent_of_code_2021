import os
import numpy as np

if __name__ == "__main__":

	# Change this to match name of input file with data
	FILENAME = 'input.txt'

	# Current Directory
	pwd = os.getcwd()

	# Check if input file exists in base folder
	if FILENAME in os.listdir(pwd):

		#Read data in, line by line
		with open(FILENAME, 'r') as infile:
			data = infile.readlines()
		
		# Clean data and cast to int
		data = [int(elem) for elem in data[0].split(',')] 
		
		numCrabs = len(data)
		bestCost = max(data)*numCrabs
		bestTarget = 0
		for i in range(numCrabs):
			cost = 0
			target = data[i]
			for j in range(numCrabs):
				cost += abs(data[j] - target)

			if cost < bestCost:
				bestCost = cost 
				bestTarget = target

		print(bestCost, bestTarget)


	else:
		raise(AssertionError("$s not found in $s" % (FILENAME, pwd)))