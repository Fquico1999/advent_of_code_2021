import os
import numpy as np

class Line():
	def __init__(self, x1,y1,x2,y2):
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2
		self.setOrientation()

	def setOrientation(self):
		if self.x1 == self.x2:
			self.orientation = 'vertical'
			self.static_dim = self.x1
		elif self.y1 == self.y2:
			self.orientation = 'horizontal'
			self.static_dim = self.y1
		else:
			self.orientation = 'diagonal'
			self.static_dim = None

	def __str__(self):
		return "(%i, %i,) -> (%i, %i) (%s)" % (self.x1, self.y1, self.x2, self.y2, self.orientation)

def intersection(LineA, LineB):

	intersections = []

	#Check if only straight lines
	if LineA.orientation not in ['horizontal', 'vertical'] or LineB.orientation not in ['horizontal', 'vertical']:
		return intersections

	# Matching orientations = No intersection or fully intersecting
	if LineA.orientation == LineB.orientation:
		if LineA.orientation == 'horizontal':
			if LineA.static_dim == LineB.static_dim:
				xmin = max(LineA.x1, LineB.x1)
				xmax = min(LineA.x2, LineB.x2)
				for i in range(xmax - xmin+1):
					intersections.append( (xmin+i, LineA.static_dim))
				return intersections
			else:
				return intersections
		if LineA.orientation == 'vertical':
			if LineA.static_dim == LineB.static_dim:
				ymin = max(LineA.y1, LineB.y1)
				ymax = min(LineA.y2, LineB.y2)
				for i in range(ymax-ymin+1):
					intersections.append((LineA.static_dim, ymin+i))
				return intersections
			else:
				return intersections
	else:
		x_int = -1
		y_int = -1
		if LineA.orientation == "horizontal":

			#Check if LineB is intersecting
			if (LineB.y1 <= LineA.static_dim) and (LineB.y2 >= LineA.static_dim):
				y_int = LineA.static_dim
			if (LineA.x1 <= LineB.static_dim) and (LineA.x2 >= LineB.static_dim):
				x_int = LineB.static_dim
			
		if LineA.orientation == 'vertical':
			#Check if LineB is intersecting
			if (LineA.y1 <= LineB.static_dim) and (LineA.y2 >= LineB.static_dim):
				y_int = LineB.static_dim
			if (LineB.x1 <= LineA.static_dim) and (LineB.x2 >= LineA.static_dim):
				x_int = LineA.static_dim
		intersections = (x_int, y_int)
		if -1 in intersections:
			return []
		else:
			return [intersections]


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
			line = Line(int(x1),int(y1),int(x2),int(y2))
			lines.append(line)

		for i, LineA in enumerate(lines):
			for j in range(i):
				if i != j:
					LineB = lines[j]
					isection = intersection(LineA, LineB)
					if isection:
						for elem in isection:
							if str(elem) not in intersections.keys():
								intersections[str(elem)] = 2
							else:
								intersections[str(elem)]+=1
		print(len(intersections))

	else:
		raise(AssertionError("$s not found in $s" % (FILENAME, pwd)))