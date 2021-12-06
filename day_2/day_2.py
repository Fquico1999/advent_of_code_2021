import os

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
		
		# Each element in data is a command string followed by an integer 
		# Note that we only care about up/down and left/right, since these are orthogonal directions. Label as x,y
		x = 0
		y = 0

		for elem in data:
			cmd, step = elem.rstrip().split(' ')
			
			if cmd == "up":
				y -= int(step) # Here we define y as depth, so higher y means deeper
			elif cmd == "down":
				y += int(step)
			elif cmd == "forward":
				x+= int(step)

		print(x,y)
		print(x*y)
		
		

	else:
		raise(AssertionError("$s not found in $s" % (FILENAME, pwd)))
	