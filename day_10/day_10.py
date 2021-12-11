import os
import numpy as np
import matplotlib.pyplot as plt

def part1(data):

	score = 0
	scores = {')':3, ']':57, '}':1197, '>':25137}
	closing = [')',']','}','>']
	opening = ['(','[','{','<']

	for line in data:
		stack = []

		for elem in list(line):
			if elem in opening:
				stack.append(elem)
			elif elem in closing:
				poped = stack.pop()
				closingIdx = closing.index(elem)
				openingIdx = opening.index(poped)
				if closingIdx != openingIdx:
					score += scores[elem]
	return score



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
		data = [line.strip() for line in data]
		

		print(part1(data))


	else:
		raise(AssertionError("$s not found in $s" % (FILENAME, pwd)))