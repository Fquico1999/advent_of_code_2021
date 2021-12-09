import os
import numpy as np
import matplotlib.pyplot as plt
from functools import reduce

def part1(heightmap):

	localMin = []
	indices = []
	paddedHeightmap = np.pad(heightmap,1,'maximum')
	lenY, lenX = paddedHeightmap.shape

	for i in range(lenY-2):

		for j in range(lenX-2):
			#Check row above
			if (paddedHeightmap[i+1, j+1] < paddedHeightmap[i,j+1]) and (paddedHeightmap[i+1, j+1] < paddedHeightmap[i+2,j+1]) and(paddedHeightmap[i+1, j+1] < paddedHeightmap[i+1,j]) and (paddedHeightmap[i+1, j+1] < paddedHeightmap[i+1,j+2]):
				localMin.append(paddedHeightmap[i+1,j+1])
				indices.append([i+1, j+1])
				#print(paddedHeightmap[i:i+3, j:j+3])
	#print(localMin)
	return(indices, sum(np.add(localMin,1)))

def fillBasin(i,j,heightmap, area):
	# toShow = np.copy(heightmap)
	# toShow[i,j] = -2
	# print(toShow)
	reachedEnd = True
	if heightmap[i-1, j] == 1:
		#prevent going back
		heightmap[i,j] = -1
		area=fillBasin(i-1, j, heightmap, area)
	if heightmap[i+1, j] == 1:
		#prevent going back
		heightmap[i,j] = -1
		area=fillBasin(i+1, j, heightmap, area)
	if heightmap[i, j-1] == 1:
		#prevent going back
		heightmap[i,j] = -1
		area=fillBasin(i, j-1, heightmap, area)
	if heightmap[i, j+1] == 1:
		#prevent going back
		heightmap[i,j] = -1
		area=fillBasin(i, j+1, heightmap, area)

	if reachedEnd:
		heightmap[i,j] = -1
		return area+1

def part2(heightmap):
	localMin = []
	paddedHeightmap = np.pad(heightmap,1,'maximum')
	lenY, lenX = paddedHeightmap.shape

	# Get indices of lowest points
	indices, _ = part1(heightmap)

	mask = np.copy(paddedHeightmap)
	mask[mask < 9] = 1
	mask[mask == 9] = 0
	print(mask)

	areas = []

	for i,j in indices:
		areas.append(fillBasin(i,j,mask.copy(), 0))

	print("\nThree Largest Basin Areas:")
	print(sorted(areas)[-3:])
	print(reduce(lambda x,y: x*y, sorted(areas)[-3:]))


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
		# Load 2D heightmap
		data = [np.asarray(list(elem.strip()), dtype=int) for elem in data] 
		data = np.asarray(data)

		#print(part1(data))

		part2(data)

		### PART 1 ###
		#bestCost = grad_descent(data, part1_cost, part1_grad)

		### PART 2 ###


	else:
		raise(AssertionError("$s not found in $s" % (FILENAME, pwd)))