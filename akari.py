# Santiago Quintero
# Edgar Amezquita

class Akari:
	"""docstring for akari
	   0 - celda blanca sin bombilla
	   1 - celda blanca con bombilla
	   2 - celda negra sin numero
	   3,4,5,6,7 - celda negra con numero
	   8 - celda blanca donde no puede haber bombilla
	   9 - celda blanca iluminada
	"""
	def __init__(self):
		filename = raw_input("Ingrese el nombre del archivo: ")
		file = open(filename, 'r')
		data= file.readline().split(" ")
		data = [int(x) for x in data]
		self.x = data[0]
		self.y = data[1]
		self.matrix = []
		for x in xrange(data[0]):
			tmp = [int(x) for x in file.readline().split(" ")]
			self.matrix.append(tmp)
		
	def iluminate(self, mx, my):
		self.matrix[mx][my] = 1
		# mark with 9 up
		for x in xrange(mx,-1,-1):
			if self.matrix[x][my] >= 2 and self.matrix[x][my] <= 7:
				break
			if self.matrix[x][my] == 0 or self.matrix[x][my] == 8:
				self.matrix[x][my] = 9
		# mark with 9 down
		for x in xrange(mx, self.x):
			if self.matrix[x][my] >= 2 and self.matrix[x][my] <= 7:
				break
			if self.matrix[x][my] == 0 or self.matrix[x][my] == 8:
				self.matrix[x][my] = 9
		# mark with 9 left
		for y in xrange(my,-1,-1):
			if self.matrix[mx][y] >= 2 and self.matrix[mx][y] <= 7:
				break
			if self.matrix[mx][y] == 0 or self.matrix[mx][y] == 8:
				self.matrix[mx][y] = 9
		# mark with 9 right
		for y in xrange(my, self.y):
			if self.matrix[mx][y] >= 2 and self.matrix[mx][y] <= 7:
				break
			if self.matrix[mx][y] == 0 or self.matrix[mx][y] == 8:
				self.matrix[mx][y] = 9

	def putBulb(self, x, y):
		if x >= 0 and x < self.x and y >= 0 and y < self.y:
			self.iluminate(x, y)

	def putZero(self, x, y):
		if x >= 0 and x < self.x and y >= 0 and y < self.y:
			if(self.matrix[x][y] == 0):
				self.matrix[x][y] = 8

	def solveFour(self):
		for x in xrange(self.x):
			for y in xrange(self.y):
				if self.matrix[x][y] == 7:
					self.putBulb(x-1, y)
					self.putBulb(x+1, y)
					self.putBulb(x, y-1)
					self.putBulb(x, y+1)

	def solveZero(self):
		for x in xrange(self.x):
			for y in xrange(self.y):
				if self.matrix[x][y] == 3:
					self.putZero(x-1,y)
					self.putZero(x+1,y)
					self.putZero(x,y-1)
					self.putZero(x,y+1)

	def check(self, x, y):
		if x >= 0 and x < self.x and y >= 0 and y < self.y:
			if self.matrix[x][y] == 0:
				return 0
			if self.matrix[x][y] == 1:
				return 1
		return -1

	def solveNumber(self, n):
		count = 0
		iluminated = 0
		found = False
		for x in xrange(self.x):
			for y in xrange(self.y):
				if self.matrix[x][y] == n + 3:		
					count = 0
					iluminated = 0
					if self.check(x-1, y) == 0:
						count += 1
					if self.check(x+1, y) == 0:
						count += 1
					if self.check(x, y-1) == 0:
						count += 1
					if self.check(x, y+1) == 0:
						count += 1
					if self.check(x-1, y) == 1:
						iluminated += 1
					if self.check(x+1, y) == 1:
						iluminated += 1
					if self.check(x, y-1) == 1:
						iluminated += 1
					if self.check(x, y+1) == 1:
						iluminated += 1
					if count + iluminated == n and iluminated < n:
						found = True
						if self.check(x-1, y) == 0:
							self.putBulb(x-1, y)
						if self.check(x+1, y) == 0:
							self.putBulb(x+1, y)
						if self.check(x, y-1) == 0:
							self.putBulb(x, y-1)
						if self.check(x, y+1) == 0:
							self.putBulb(x, y+1)
		return found

	def printMatrix(self):
		for row in self.matrix:
			print row

	def solveAkari(self):
		#show initial state
		print ""
		print "=================[Input]====================="
		print ""
		self.printMatrix()
		# check for black with 0
		self.solveZero()
		# check for black with 4
		self.solveFour()
		# check for black with 1,2,3 until no more bulbs can be trivially put
		found = True
		while found:
			found = False
			for x in xrange(1,4):
				if self.solveNumber(x):
					found = True
		# print the final state
		print ""
		print "=================[Result]====================="
		print ""
		self.printMatrix()



akari = Akari()
akari.solveAkari()
	
