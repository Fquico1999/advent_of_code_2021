import os
import numpy as np
import matplotlib.pyplot as plt

FILENAME = 'input.txt'

if __name__ == "__main__":

	# Change this to match name of input file with data

	# Current Directory
	pwd = os.getcwd()

	# Check if input file exists in base folder
	if FILENAME in os.listdir(pwd):

		#Read data in, line by line
		with open(FILENAME, 'r') as infile:
			data = infile.readlines()

		data = [line.strip() for line in data]

		template = data[0]
		insertionRules = data[2:] # Start at 2 to avoid space
		for i, rule in enumerate(insertionRules):
			match, insert = rule.split(' -> ')
			insertionRules[i] = [match, insert]

		
		NUMSTEPS = 10
		polymer = list(template)
		print("Template:\t\t\t%s" % ''.join(polymer))
		for step in range(NUMSTEPS):
			count_dict = {}
			output = polymer.copy()
			polymerLength = len(polymer)
			j = 0
			for i in range(polymerLength-1):
				pair = ''.join(polymer[i:i+2])
				for rule in insertionRules:
					match, insert = rule 
					if match == pair:
						output.insert(j+1, insert)
						j+=1
				j+=1

				#print(''.join(output))
			print("After %i steps:\t\t%s" % (step+1, ''.join(output)))
			
			for elem in output:
				if elem not in count_dict.keys():
					count_dict[elem] = 1
				else:
					count_dict[elem]+=1

			sorted_dict = dict(sorted(count_dict.items(), key=lambda item: item[1]))
			score = list(sorted_dict.values())[-1] - list(sorted_dict.values())[0]
			print(score)
			polymer = output

		
		
		


	else:
		raise(AssertionError("$s not found in $s" % (FILENAME, pwd)))