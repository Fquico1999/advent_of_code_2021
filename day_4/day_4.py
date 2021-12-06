import os
import numpy as np

class BingoBoard():

	def __init__(self, size):
		self.size = size
		self.board = np.zeros(size, size)
		self.marked = np.zeros(size, size)

	def __init__(self, size, initial_state):
		self.size = size
		self.board = initial_state
		self.marked = np.zeros([size, size])

	def __str__(self):
		ret = []
		for i in range(self.size):
			for j in range(self.size):
				if self.marked[i,j]:
					ret.append(" *%2i* " % self.board[i,j])
				else:
					ret.append("%4i" % self.board[i,j])

			ret.append("\n")
		return "".join(ret)

	def checkNumber(self, num):
		# Check if number is on board and unmarked
		idx = np.squeeze(np.where(self.board[:,:] == num))
		if idx.any():
			x,y = idx
			# Mark number on board
			self.marked[x,y] = 1

	def checkWin(self):
		# If there is a winning row, return True and [i,-1] where i is the index of the winning row.
		# If there is a winning col, return True and [-1,i] where i is the index of the winning col.

		for i in range(self.size):
			# If the elements of a row or column multiplied are 1, means that row/col has been filled.
			r = np.prod(self.marked[i,:])
			c = np.prod(self.marked[:,i])
			if r:
				return True, [i,-1]
			if c:
				return True, [-1,i]

		return False, [-1,-1]

	def computeScore(self, num):
		unmarked = self.board[self.marked == 0]
		score = num*np.sum(unmarked)
		return score


if __name__ == "__main__":

	# Change this to match name of input file with data
	FILENAME = 'input.txt'

	# Current Directory
	pwd = os.getcwd()

	# Check if input file exists in base folder
	if FILENAME in os.listdir(pwd):

		# Get each line of data
		with open(FILENAME, 'r') as infile:
			data = infile.readlines()

		# Clean data
		data = [elem.rstrip() for elem in data]

		numbers = [int(elem) for elem in data[0].split(',')]
		boards = [line.strip().split() for line in data[1:] if line ] # Filter out empty lines
		board_size = len(boards[1])
		num_boards = len(boards)//board_size

		bingo_boards = []
		winning_board = None
		winning_score = 0
		finished = False

		# Extract inital state of all boards and initialize BingoBoards for each
		for idx in range(num_boards):
			# Get initial state of the board
			initial_state = np.asarray([boards[idx*board_size+j] for j in range(board_size)], dtype=int)

			# Create BingoBoard object with initial state
			bboard = BingoBoard(board_size, initial_state)
			bingo_boards.append(bboard)
		for num in numbers:
			for bingo_board in bingo_boards:
				bingo_board.checkNumber(num)
				won, idx = bingo_board.checkWin()
				if won:
					score = bingo_board.computeScore(num)
					if score > winning_score:
						winning_score = score 
						winning_board = bingo_board
					bingo_boards.remove(bingo_board)
					finished = True
			
			if finished:
				break


		print(winning_score)
		print(winning_board)
	else:
		raise(AssertionError("$s not found in $s" % (FILENAME, pwd)))