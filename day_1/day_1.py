
# Day 1
import os

def num_increased(data):
	increased_count = 0 

	for idx in range(len(data)-1):
		if data[idx+1] > data[idx]:
			increased_count+=1

	return increased_count


def part1(FILENAME):
	#Read data in, line by line
	with open(FILENAME, 'r') as infile:
		data = infile.readlines()
	
	# Clean data and cast to int
	data = [int(elem.rstrip()) for elem in data]
	
	increased_count = num_increased(data)
	

def part2(FILENAME):
	#Read data in, line by line
	with open(FILENAME, 'r') as infile:
		data = infile.readlines()
	
	# Clean data and cast to int
	data = [int(elem.rstrip()) for elem in data]

	# How many points do we get with a three element sliding window?
	numpoints = len(data) - (3-1)

	sliding_sum = []

	for idx in range(numpoints):
		sliding_sum.append(data[idx] + data[idx+1] + data[idx+2])

	print(sliding_sum)

if __name__ == "__main__":

	# Change this to match name of input file with data
	FILENAME = 'input.txt'

	# Current Directory
	pwd = os.getcwd()

	# Check if input file exists in base folder
	if FILENAME in os.listdir(pwd):

		### PART 1 ###

		# Get number of times data increased from prev to current
		#Read data in, line by line
		with open(FILENAME, 'r') as infile:
			data = infile.readlines()
		
		# Clean data and cast to int
		data = [int(elem.rstrip()) for elem in data]
		
		increased_count = num_increased(data)
		print(increased_count)

		### PART 2 ###

		# How many points do we get with a three element sliding window?
		numpoints = len(data) - (3-1)

		sliding_sum = []

		for idx in range(numpoints):
			sliding_sum.append(data[idx] + data[idx+1] + data[idx+2])

		increased_count = num_increased(sliding_sum)
		print(increased_count)

	else:
		raise(AssertionError("$s not found in $s" % (FILENAME, pwd)))
	