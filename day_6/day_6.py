import os
import numpy as np
import matplotlib.pyplot as plt

def update(states):

	# New fish to spawn with timer set to 8
	temp = states[0]

	# Shift all fish down
	states[0:-1] = states[1:]

	# Fish that just spawned other fish set to 6
	states[6]+= temp

	# Spawn new fish
	states[-1]=temp

	return states

if __name__ == "__main__":

	# Change this to match name of input file with data
	FILENAME = 'input.txt'

	# Current Directory
	pwd = os.getcwd()

	states = np.zeros(9)

	# Check if input file exists in base folder
	if FILENAME in os.listdir(pwd):

		#Read data in, line by line
		with open(FILENAME, 'r') as infile:
			data = infile.readlines()
		
		# Clean data and cast to int
		initial_state = [int(elem) for elem in data[0].split(',')] 
		

		for timer in initial_state:
			states[timer] +=1
		### PART 1 ###
		#NUM_DAYS = 80
		
		### PART 2 ###
		NUM_DAYS = 256

		for t in range(NUM_DAYS):
			states = update(states)
			print(states)
			print(sum(states))
		print("\nDAY: %i   NUM FISH: %i" % (t+1, sum(states)))

	else:
		raise(AssertionError("$s not found in $s" % (FILENAME, pwd)))