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

def part2(data):
	# We score the unmatched openings to avoid extra computation
	score_dict = {'(':1, '[':2, '{':3, '<':4}
	scores = []
	closing = [')',']','}','>']
	opening = ['(','[','{','<']

	# Filter out corrupted
	corrupted_idxs = []
	for i,line in enumerate(data):
		stack = []
		for elem in list(line):
			if elem in opening:
				stack.append(elem)
			elif elem in closing:
				poped = stack.pop()
				closingIdx = closing.index(elem)
				openingIdx = opening.index(poped)
				if closingIdx != openingIdx:
					#Corrupted entry
					corrupted_idxs.append(i)

	data = [line for i, line in enumerate(data) if i not in corrupted_idxs]

	for line in data:
		score = 0
		stack = []
		for elem in list(line):
			if elem in opening:
				stack.append(elem)
			elif elem in closing:
				poped = stack.pop()
		# If stack is not empty, that means that the line is incomplete
		# Need this if statement to avoid scoring complete lines
		if stack:
			while stack:
				# Get last unclosed entry
				poped = stack.pop()
				score = score*5 + score_dict[poped]
			scores.append(score)
	scores = sorted(scores)
	return scores[len(scores)//2]


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
		
		print(part2(data))


	else:
		raise(AssertionError("$s not found in $s" % (FILENAME, pwd)))