import os
import numpy as np
import matplotlib.pyplot as plt

def part1(data):
	numCrabs = len(data)
	bestCost = max(data)*numCrabs
	bestTarget = 0
	for i in range(numCrabs):
		cost = 0
		target = data[i]
		for j in range(numCrabs):
			cost += abs(data[j] - target)

		if cost < bestCost:
			bestCost = cost 
			bestTarget = target

	return bestCost

def part1_cost(x,x_i):
	return np.sum(abs(x-x_i))/len(x)
def part1_grad(x, x_i):
	eps = 1e-7
	return np.sum((x-x_i)/(abs(x-x_i)+eps))

def part2_cost(x, x_i):
	d = abs(x-x_i)
	cost_vec = 0.5*d*(d+1)
	print(cost_vec)
	return np.sum(cost_vec)/len(x)

def part2_grad(x, x_i):
	eps = 1e-7
	d = x-x_i
	# Don't forget the absolute sign in the derivative computation
	cost_vec = 0.5 * d*(2*abs(d)+1)/abs(d+eps)
	return np.sum(cost_vec)


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



def part2(data):
	numCrabs = len(data)
	bestCost = max(data)*sum(range(numCrabs))
	bestTarget = 0
	for i in range(numCrabs):
		cost = 0
		target = i
		for j in range(numCrabs):
			cost += sum(range(abs(data[j] - target)+1))

		if cost < bestCost:
			bestCost = cost 
			bestTarget = target

	return bestCost


if __name__ == "__main__":

	# Change this to match name of input file with data
	FILENAME = 'test.txt'

	# Current Directory
	pwd = os.getcwd()

	# Check if input file exists in base folder
	if FILENAME in os.listdir(pwd):

		#Read data in, line by line
		with open(FILENAME, 'r') as infile:
			data = infile.readlines()
		
		# Clean data and cast to int
		data = [int(elem) for elem in data[0].split(',')] 
		data = np.asarray(data)
		#bestCost = part1(data)
		#bestCost = part2(data)
		
		### PART 1 ###
		#bestCost = grad_descent(data, part1_cost, part1_grad)

		### PART 2 ###
		bestCost = grad_descent(data, part2_cost, part2_grad)


	else:
		raise(AssertionError("$s not found in $s" % (FILENAME, pwd)))