import os
import numpy as np

if __name__ == "__main__":

	# Change this to match name of input file with data
	FILENAME = 'input.txt'

	# Current Directory
	pwd = os.getcwd()

	# Check if input file exists in base folder
	if FILENAME in os.listdir(pwd):

		### PART 1 ###

		# Get each line of data
		with open(FILENAME, 'r') as infile:
			data = infile.readlines()

		# Clean data
		data = [elem.rstrip() for elem in data]

		# Convert list of strings to 2D array of integers, each entry in a list of bits
		arr = np.asarray([list(elem) for elem in data], dtype=np.uint8)

		# Loop over columns to construct most common bits
		numLength = arr.shape[1]
		gamma_rate = np.zeros(numLength)
		epsilon_rate = np.zeros(numLength)

		# Loop over columns to obtain most and least common bits
		for idx in range(numLength):
			# Most common bit is the rounded average
			# I.e  mean([0,1,1,0,0,0]) = 2/6 < 0.5 ~ 0
			gamma_rate[idx] = int(round(np.mean(arr[:,idx])))
			epsilon_rate[idx] = max(abs(gamma_rate[idx] - 1), 0) # Flip bit

		# Convert integers to strings to assemble the binary digits
		gamma_rate = [str(int(bit)) for bit in gamma_rate]
		epsilon_rate = [str(int(bit)) for bit in epsilon_rate]

		# Convert rates to decimal
		gamma_rate = int('0b' + ''.join(gamma_rate), 2)
		epsilon_rate =  int('0b' + ''.join(epsilon_rate),2)

		power_consumption = gamma_rate*epsilon_rate
		#print(power_consumption)


		### PART 2 ###

		def filter(arr, idx, crit):
			avg = np.mean(arr[:,idx])
			if avg >= 0.5:
				# Default round will round 0.5 to nearest even, not the desired behaviour
				bit = 1
			else:
				bit = 0

			if crit == 'least':
				bit = max(abs(bit-1), 0)

			arr = arr[arr[:,idx] == bit]
			if arr.shape[0] == 1:
				# We only have one entry - basecase - return the number
				return arr[0]
			elif idx == arr.shape[1]:
				# Reached the end
				return arr
			else:
				return filter(arr, idx+1, crit)

		o2_gen_rating = filter(arr, 0, 'most')
		co2_scrub_rating = filter(arr, 0, 'least')


		# Convert integers to strings to assemble the binary digits
		o2_gen_rating = [str(int(bit)) for bit in o2_gen_rating]
		co2_scrub_rating = [str(int(bit)) for bit in co2_scrub_rating]

		# Convert rates to decimal
		o2_gen_rating = int('0b' + ''.join(o2_gen_rating), 2)
		co2_scrub_rating =  int('0b' + ''.join(co2_scrub_rating),2)

		life_support_rating = co2_scrub_rating*o2_gen_rating
		print(life_support_rating)

	else:
		raise(AssertionError("$s not found in $s" % (FILENAME, pwd)))