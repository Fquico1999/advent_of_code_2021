import os
import numpy as np
import matplotlib.pyplot as plt

class TransparentPaper():
	def __init__(self, points):
		self.width = max(points[:,0])+1
		self.height = max(points[:,1])+1
		self.state = self.setState(points)

	def setState(self, points):
		state = np.zeros([self.height, self.width])
		for point in points:
			# X and Y are actually flipped here, x increases col and y increases row
			xi, yi = point[::-1]
			state[xi,yi] = 1
		return state

	def fold(self, loc, axis):
		# Axis = 0 fold in y
		if axis == 0:
			numRows = self.height - loc+1
			# If the number of rows to fold up is greater than the upper rows, cap it.
			numRows = min(loc+1, numRows)
			for i in range(numRows):
				self.state[loc-i, :] += self.state[loc+i, :]

			self.state = self.state[:loc, :]

		# Axis = 1 fold in x
		elif axis == 1:
			numCols = self.width - loc+1
			# If the number of cols to fold left is greater than the upper rows, cap it.
			numCols = min(loc+1, numCols)
			for i in range(numCols):
				self.state[:,loc-i] += self.state[:,loc+i]
			self.state = self.state[:,:loc]

		self.state[self.state > 1] = 1

	def numVisibile(self):
		return np.sum(self.state  == 1)

	def plot(self):
		fig, ax = plt.subplots()
		ax.imshow(self.state)
		plt.show()

	def __str__(self):
		return str(self.state) + "\n"


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
		
		# Get points on map
		points = []
		for i, entry in enumerate(data):
			if entry == "\n":
				break
			x,y = entry.rstrip().split(",")
			points.append([int(x), int(y)])
		points = np.asarray(points, dtype=int)
		# Get fold instructions
		folds = []
		for j in range(i+1, len(data)):
			fold = data[j].rstrip().split("fold along")[-1]
			axis, num = fold.split("=")
			if axis.strip() == 'x':
				folds.append([int(num), 1])
			elif axis.strip() == 'y':
				folds.append([int(num), 0])
			
		#print(points)
		
		paper = TransparentPaper(points)
		for fold in folds:
			#print(paper)
			paper.fold(fold[0], fold[1])
			print(paper)
			#print(paper.numVisibile())
		paper.plot()
		


		#print(data)
		#data = [list(line.rstrip()) for line in data]
		
		#print(data)
		
		#part1(data)


	else:
		raise(AssertionError("$s not found in $s" % (FILENAME, pwd)))