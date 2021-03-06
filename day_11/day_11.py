import os
import numpy as np
import matplotlib.pyplot as plt

def part1(grid):

	sizeX, sizeY = grid.shape
	ones = np.ones([sizeX, sizeY], dtype=int)
	NUMSTEPS = 100
	numFlashes = 0
	print("INITIAL STATE:")
	print(grid)
	for i in range(NUMSTEPS):
		print("STEP %i" % i)
		# Increment all by one
		print(grid)
		print("\n")
		grid += ones

		# Check for energy level 10 or higher
		
		while np.sum(grid > 9):
			indices = np.where(grid > 9)
			for x,y in zip(indices[0], indices[1]):
				# Add to count
				numFlashes += 1 

				# Set to -1 to avoid double flashing
				grid[x,y] = -1

				# Increment neighbouring tiles that are not -1
				mask = np.zeros([sizeX, sizeY], dtype=bool)
				xmin = max(0, x-1)
				xmax = min(sizeX+1, x+2)
				ymin = max(0, y-1)
				ymax = min(sizeY+1, y+2)
				mask[xmin:xmax, ymin:ymax] = grid[xmin:xmax, ymin:ymax] != -1
				grid[mask] += 1
			indices = np.where(grid > 9)

		# Set -1's to zero
		grid[grid == -1] = 0


		print(numFlashes)

def part2(grid):
	sizeX, sizeY = grid.shape
	ones = np.ones([sizeX, sizeY], dtype=int)
	step = 0
	allFlashed = False
	while not allFlashed:
		# Increment all by one
		print(grid)
		print("\n")
		grid += ones

		# Check for energy level 10 or higher
		
		while np.sum(grid > 9):
			indices = np.where(grid > 9)
			for x,y in zip(indices[0], indices[1]):

				# Set to -1 to avoid double flashing
				grid[x,y] = -1

				# Increment neighbouring tiles that are not -1
				mask = np.zeros([sizeX, sizeY], dtype=bool)
				xmin = max(0, x-1)
				xmax = min(sizeX+1, x+2)
				ymin = max(0, y-1)
				ymax = min(sizeY+1, y+2)
				mask[xmin:xmax, ymin:ymax] = grid[xmin:xmax, ymin:ymax] != -1
				grid[mask] += 1
			indices = np.where(grid > 9)

		if np.sum(grid-ones) == 0:
			allFlashed = True
		else:
			# Set -1's to zero
			grid[grid == -1] = 0
			step+=1


		print(step)


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
		data = [list(line.rstrip()) for line in data]
		data = np.asarray(data, dtype=int)
		
		#part1(data)
		part2(data)


	else:
		raise(AssertionError("$s not found in $s" % (FILENAME, pwd)))