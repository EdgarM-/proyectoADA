class Posicion:
	"""docstring for Posicion"""
	def __init__(self, x,y):
		self.x = x
		self.y = y
		

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

	def functionT(self,mx,my):	# la funcionT devuelve las posiciones que estan dentro del tablero y no son cajas negras, alrededor del posicion x,y
		posiciones = []
		if mx >= 0 and mx < self.x and my >= 0 and my < self.y:
			if self.matrix[mx-1][my] > 1 and self.matrix[mx-1][my] < 8:
				pos = Posicion(mx-1,my)
				posiciones.append(pos)
			if self.matrix[mx+1][my] > 1 and self.matrix[mx+1][my] < 8:
				pos = Posicion(mx+1,my)
				posiciones.append(pos)
			if self.matrix[mx][my-1] > 1 and self.matrix[mx][my-1] < 8:
				pos = Posicion(mx,my-1)
				posiciones.append(pos)
			if self.matrix[mx][my+1]  > 1 and self.matrix[mx][my+1] < 8:
				pos = Posicion(mx,my+1)
				posiciones.append(pos)
		return posiciones

	def functionB(self, posiciones): # Verifica la puesta de un bombillo es decir que no haya un bombillo en la casilla y que no este iluminado
		apPosiciones = []
		for pos in posiciones:
			if self.matrix[pos.x][pos.y] = 0 :
				apPosiciones.append(pos)
		return apPosiciones

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

	def deIluminate(self, mx, my):
		self.matrix[mx][my] = 0
		# mark with 9 up
		for x in xrange(mx,-1,-1):
			if self.matrix[x][my] >= 2 and self.matrix[x][my] <= 7:
				break
			if self.matrix[x][my] == 0 or self.matrix[x][my] == 8:
				self.matrix[x][my] = 0
		# mark with 9 down
		for x in xrange(mx, self.x):
			if self.matrix[x][my] >= 2 and self.matrix[x][my] <= 7:
				break
			if self.matrix[x][my] == 0 or self.matrix[x][my] == 8:
				self.matrix[x][my] = 0
		# mark with 9 left
		for y in xrange(my,-1,-1):
			if self.matrix[mx][y] >= 2 and self.matrix[mx][y] <= 7:
				break
			if self.matrix[mx][y] == 0 or self.matrix[mx][y] == 8:
				self.matrix[mx][y] = 0
		# mark with 9 right
		for y in xrange(my, self.y):
			if self.matrix[mx][y] >= 2 and self.matrix[mx][y] <= 7:
				break
			if self.matrix[mx][y] == 0 or self.matrix[mx][y] == 8:
				self.matrix[mx][y] = 0