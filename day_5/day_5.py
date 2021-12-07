import os
import numpy as np

def drawLine(line, grid):
	x1,y1,x2,y2 = line

	if x2 > x1:
		dx = 1
	elif x2 == x1:
		dx = 0
	else:
		dx = -1

	if y2 > y1:
		dy = 1
	elif y2 == y1:
		dy = 0
	else:
		dy = -1

	x = x1
	y = y1
	while((x != x2) or (y != y2)):
		grid[y,x] += 1
		x+=dx
		y+=dy
	grid[y,x] += 1
	return grid


if __name__ == "__main__":

	# Change this to match name of input file with data
	FILENAME = 'input.txt'

	# Current Directory
	pwd = os.getcwd()

	intersections = {}

	# Check if input file exists in base folder
	if FILENAME in os.listdir(pwd):

		with open(FILENAME, 'r') as infile:
			data = infile.readlines()
		
		# Clean data and cast to int
		data = [elem.split(' -> ') for elem in data]

		lines = []

		for i, line in enumerate(data):
			x1,y1 = line[0].split(',')
			x2,y2 = line[1].split(',')
			lines.append(np.asarray([x1,y1,x2,y2], dtype=int))

		lines = np.asarray(lines)
		xmax = max(np.max(lines[:,0]), np.max(lines[:,2]))
		ymax = max(np.max(lines[:,1]), np.max(lines[:,3]))

		grid = np.zeros([xmax+1, ymax+1])

		### PART 1 ###
		# for line in lines:
		# 	# For part one, only draw horizontal / vertical lines
		# 	if (line[0] == line[2]) or (line[1] ==line[3]):
		# 		grid = drawLine(line, grid)
		# numDangerous = np.sum(grid[:,:] >= 2)
		# print(numDangerous)

		### PART 2 ###
		for line in lines:
			grid = drawLine(line, grid)
		numDangerous = np.sum(grid[:,:] >= 2)
		print(numDangerous)
	else:
		raise(AssertionError("$s not found in $s" % (FILENAME, pwd)))