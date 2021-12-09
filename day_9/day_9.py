import os
import numpy as np
import matplotlib.pyplot as plt

def part1(heightmap):

	localMin = []
	paddedHeightmap = np.pad(heightmap,1,'maximum')
	lenY, lenX = paddedHeightmap.shape

	for i in range(lenY-2):

		for j in range(lenX-2):
			#Check row above
			if (paddedHeightmap[i+1, j+1] < paddedHeightmap[i,j+1]) and (paddedHeightmap[i+1, j+1] < paddedHeightmap[i+2,j+1]) and(paddedHeightmap[i+1, j+1] < paddedHeightmap[i+1,j]) and (paddedHeightmap[i+1, j+1] < paddedHeightmap[i+1,j+2]):
				localMin.append(paddedHeightmap[i+1,j+1])
				#print(paddedHeightmap[i:i+3, j:j+3])
	#print(localMin)
	return(sum(np.add(localMin,1)))


def grad_descent(data, cost, grad):
	numCrabs = len(data)
	bestCost = max(data)*numCrabs
	bestTarget = 0

	# Normalize data
	data_min = min(data)
	data_max = max(data)
	data_norm = (data - data_min)/data_max

	# First Guess is random between 0 and 1 - vectorized
	x = np.ones(numCrabs)*np.random.random(1)
	print("Initial Guess: %f" % x[0])

	# "Learning Rate" and epochs
	alpha = 0.0001
	epochs = 1000

	# For display
	c_arr = []
	x_arr = []

	for e in range(epochs):
		print("EPOCH: %i" % e)

		# Compute cost
		c = cost(x,data_norm)
		c_arr.append(c)

		# Compute grad
		dx = grad(x, data_norm)
		
		# Update
		x = x - alpha*dx
		x_arr.append(x[0])

	print("FINAL X: %.2f" % x[0])
	print("SCALED X: %i"  % round(x[0]*data_max))
	scaled_x = round(x[0]*data_max)
	final_cost = cost(np.ones(numCrabs)*scaled_x, data)
	print("COST: %i" % round(final_cost*numCrabs))

	fig, ax = plt.subplots()
	fig.set_size_inches(12,12)
	ax.plot(range(epochs), c_arr, label='Cost')
	ax.plot(range(epochs), x_arr, label='x')
	ax.legend(loc='upper left')
	ax2 = plt.twinx()
	ax2.plot(range(epochs), np.multiply(data_max,x_arr), label='scaled x')
	ax2.legend()
	ax.set_ylim([0,1])
	ax2.set_ylim([0,data_max])
	plt.show()

	return final_cost


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

		print(part1(data))

		### PART 1 ###
		#bestCost = grad_descent(data, part1_cost, part1_grad)

		### PART 2 ###


	else:
		raise(AssertionError("$s not found in $s" % (FILENAME, pwd)))