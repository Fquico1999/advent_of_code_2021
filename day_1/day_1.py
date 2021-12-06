
import os


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
		data = [int(elem.rstrip()) for elem in data]
		
		increased_count = 0 

		for idx in range(len(data)-1):
			if data[idx+1] > data[idx]:
				increased_count+=1

		print(increased_count)

	else:
		raise(AssertionError("$s not found in $s" % (FILENAME, pwd)))