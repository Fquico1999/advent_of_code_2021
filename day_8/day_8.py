import os
import numpy as np
import matplotlib.pyplot as plt
from itertools import permutations

def crackKey(entry):

	for perm in permutations('abcdefg'):
		key = {}
		for idx, char in enumerate(list('abcdefg')):
			key[char] = perm[idx]
		# if list(key.values()) == ['c', 'f', 'g', 'a', 'b', 'd', 'e']:

		validKey = True
		for signal in entry:

			#Decode
			decoded = []
			for char in list(signal):
				decoded.append(key[char])
			decoded = ''.join(sorted(decoded))
			
			# If all signals are processed and each decoded signal is in original, then the key is valid
			if decoded not in list(original.values()):
				validKey = False
				break

		if validKey:
			return key

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
		data = [elem.split(' | ') for elem in data]
		
		for i, entry in enumerate(data):
			sig, output = entry
			data[i][0] = [elem.strip() for elem in sig.split(' ')]
			data[i][1] = [elem.strip() for elem in output.split(' ')]
		data = np.asarray(data)

		### PART 1 ###
		# length -> corresponding digit5
		unique_lengths = {2:1, 4:4, 3:7, 7:8}

		unique_length_count = 0
		for entry in data:
			_, output = entry
			for digit in output:
				if len(digit) in unique_lengths.keys():
					unique_length_count+=1
		print(unique_length_count)


		### PART 2 ###
		original = {0: 'abcefg', 
					1:'cf', 
					2:'acdeg', 
					3:'acdfg', 
					4:'bcdf', 
					5:'abdfg', 
					6:'abdefg', 
					7:'acf', 
					8:'abcdefg', 
					9:'abcdfg' }

		signals = [sig for sig, _ in data]
		outputs = [out for _, out in data]
		keys = []
		for entry in signals:
			keys.append(crackKey(entry))

		total = 0
		for key, output in zip(keys, outputs):
			digits = []
			for encoded_digit in output:
				#decode
				decoded = []
				for char in list(encoded_digit):
					decoded.append(key[char])
				decoded = ''.join(sorted(decoded))
				digits.append(list(original.keys())[list(original.values()).index(decoded)])
			print(digits)
			total += digits[0]*1000 + digits[1]*100 + digits[2]*10 + digits[3]
		print(total)


	else:
		raise(AssertionError("%s not found in %s" % (FILENAME, pwd)))