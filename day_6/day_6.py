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
		state = [int(elem) for elem in data[0].split(',')] 
		
		
		NUM_DAYS = 80
		print("INITIAL STATE")
		print(state)

		for t in range(NUM_DAYS):
			# Array to store new fish while current state is being processed - don't want to process new fish untill next turn
			newFish = []
			for idx, fishTimer in enumerate(state):
				fishTimer -=1
				if fishTimer < 0:
					state[idx] = 6
					newFish.append(8)
				else:
					state[idx] = fishTimer
			# Add any new fish
			state = state + newFish
		print("\nDAY: %i   NUM FISH: %i" % (t+1, len(state)))


	else:
		raise(AssertionError("$s not found in $s" % (FILENAME, pwd)))