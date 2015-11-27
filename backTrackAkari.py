# Santiago Quintero
# Edgar Amezquita
"""                                     
   d888888o.       ,o888888o.        
 .`8888:' `88.  . 8888     `88.      
 8.`8888.   Y8 ,8 8888       `8b     
 `8.`8888.     88 8888        `8b    
  `8.`8888.    88 8888         88    
   `8.`8888.   88 8888     `8. 88    
    `8.`8888.  88 8888      `8,8P    
8b   `8.`8888. `8 8888       ;8P     
`8b.  ;8.`8888  ` 8888     ,88'8.    
 `Y8888P ,88P'     `8888888P'  `8.   
                                     
8 8888888888            .8.          
8 8888                 .888.         
8 8888                :88888.        
8 8888               . `88888.       
8 888888888888      .8. `88888.      
8 8888             .8`8. `88888.     
8 8888            .8' `8. `88888.    
8 8888           .8'   `8. `88888.   
8 8888          .888888888. `88888.  
8 888888888888 .8'       `8. `88888. 
"""


class Posicion:
	"""docstring for Posicion"""
	def __init__(self, x,y):
		self.x = x
		self.y = y
		

class AkariBacktracking:
	"""docstring for akari
	   0 - celda blanca sin bombilla
	   1 - celda blanca con bombilla
	   2 - celda negra sin numero
	   3,4,5,6,7 - celda negra con numero
	   9 - celda blanca iluminada
	"""
	def __init__(self):
		filename = input("Ingrese el nombre del archivo: ")
		file = open(filename, 'r')
		data= file.readline().split(" ")
		data = [int(x) for x in data]
		self.x = data[0]
		self.y = data[1]
		self.matrix = []
		for x in range(data[0]):
			tmp = [int(x) for x in file.readline().split(" ")]
			self.matrix.append(tmp)
			
	def check(self, x, y):
		if x >= 0 and x < self.x and y >= 0 and y < self.y:
			if self.matrix[x][y] == 0:
				return 0
			if self.matrix[x][y] == 1:
				return 1
		return -1
	#Revisa que pasa si ilumino la posicion y me dice si afecta a algun numero hacia arriba	
	def checkUp(self,mx,my):
		for x in range(mx,-1,-1):
			if (self.matrix[x][my] >= 2 and self.matrix[x][my] <= 7):
				if(self.matrix[x][my] >= 4 and self.matrix[x][my] <= 7):
					return self.checkNumber(x,my)
				if(self.matrix[x][my] >= 2 and self.matrix[x][my] < 4):
					return True
		return True
	#Revisa que pasa si ilumino la posicion y me dice si afecta a algun numero hacia abajo	
	def checkDown(self,mx,my):
		for x in range(mx, self.x):
			if self.matrix[x][my] >= 2 and self.matrix[x][my] <= 7:
				if(self.matrix[x][my] >= 4 and self.matrix[x][my] <= 7):
					return self.checkNumber(x,my)
				if(self.matrix[x][my] >= 2 and self.matrix[x][my] < 4):
						return True
		return True
	#Revisa que pasa si ilumino la posicion y me dice si afecta a algun numero en la columna de la derecha	
	def checkRightCol(self,mx,my):
		return (self.checkUp(mx,my+1) and self.checkDown(mx,my+1))
	#Revisa que pasa si ilumino la posicion y me dice si afecta a algun numero en la columna de la izquierda
	def checkLeftCol(self,mx,my):
		return (self.checkUp(mx,my-1) and self.checkDown(mx,my-1))
	#Revisa que pasa si ilumino la posicion y me dice si afecta a algun numero hacia la derecha
	def checkRight(self,mx,my):
		for y in range(my, self.y):
			if self.matrix[mx][y] >= 2 and self.matrix[mx][y] <= 7:
				if(self.matrix[mx][y] >= 4 and self.matrix[mx][y] <= 7):
					return self.checkNumber(mx,y)
				if(self.matrix[mx][y] >= 2 and self.matrix[mx][y] < 4):
						return True
		return True
	#Revisa que pasa si ilumino la posicion y me dice si afecta a algun numero hacia la izquierda	
	def checkLeft(self,mx,my):
		for y in range(my,-1,-1):
			if self.matrix[mx][y] >= 2 and self.matrix[mx][y] <= 7:
				if(self.matrix[mx][y] >= 4 and self.matrix[mx][y] <= 7):
					return self.checkNumber(mx,y)
				if(self.matrix[mx][y] >= 2 and self.matrix[mx][y] < 4):
						return True
		return True
		
	def isNumberFull(self,mx,my):
		#Reviso que se halla completado la cantidad de bombillos que pueden estar cerca del numero
		countBulbs = 3
		if(self.check(mx+1,my) == 1):
			countBulbs += 1
		if(self.check(mx-1,my) == 1):
			countBulbs += 1
		if(self.check(mx,my+1) == 1):
			countBulbs += 1
		if(self.check(mx,my-1) == 1):
			countBulbs += 1
		if( countBulbs == self.matrix[mx][my] ):
			return False
		else:
			return True
	def checkNumber(self,mx,my):
		#Reviso que se pueda completar la cantidad de bombillos que pueden estar cerca del numero
		countBulbsAndBlanks = 2
		if(self.check(mx+1,my) == 0 or self.check(mx+1,my) == 1):
			countBulbsAndBlanks += 1
		if(self.check(mx-1,my) == 0 or self.check(mx-1,my) == 1):
			countBulbsAndBlanks += 1
		if(self.check(mx,my+1) == 0 or self.check(mx,my+1) == 1):
			countBulbsAndBlanks += 1
		if(self.check(mx,my-1) == 0 or self.check(mx,my-1) == 1):
			countBulbsAndBlanks += 1
		if( countBulbsAndBlanks >= self.matrix[mx][my] ):
			return True
		else:
			return False
	
	def functionT(self,mx,my, dir):	# la funcionT devuelve 0 o 1, devuelve 0 si ya habia bombillo, dir le indica si esta avanzando(1) o devolviendo(-1)
		posiciones = []
		if (mx >= 0 and mx < self.x and my >= 0 and my < self.y):
			if (self.matrix[mx][my] == 1):
				posiciones.append(0)
			elif(dir == 1) :
				posiciones = [0, 1]
			elif(dir == -1):
				posiciones = [1,0]
		return posiciones
	
	#Convenciones Funcion B
	# 1 Puede hacer la acción
	# 0 No puede hacer la acción
	# -1 Es una casilla que no puede modificar, siga al siguiente
	# -2 Hay falta de iluminación o no se puede ejecutar ninguna acción devuelvase
	def functionB(self, valor, mx,my): # Verifica si el valor a poner es factible
		if(valor == 1):
			if(self.matrix[mx][my] == 0):
				#Reviso si hay numero alrededor
				if(self.matrix[mx+1][my] == 7):
					return 1
				elif(self.matrix[mx+1][my] == 3):
					return 0
				elif(self.matrix[mx+1][my] == 4 or self.matrix[mx+1][my] == 5 or self.matrix[mx+1][my] == 6):
					return self.isNumberFull(mx+1,my)
					
				if(self.matrix[mx-1][my] == 7):
					return 1
				elif(self.matrix[mx-1][my] == 3):
					return 0
				elif(self.matrix[mx-1][my] == 4 or self.matrix[mx-1][my] == 5 or self.matrix[mx-1][my] == 6):
					return self.isNumberFull(mx-1,my)
				
				if(self.matrix[mx][my+1] == 7):
					return 1
				elif(self.matrix[mx][my+1] == 3):
					return 0
				elif(self.matrix[mx][my+1] == 4 or self.matrix[mx][my+1] == 5 or self.matrix[mx][my+1] == 6):
					return self.isNumberFull(mx,my+1)
				
				if(self.matrix[mx][my-1] == 7):
					return 1
				elif(self.matrix[mx][my-1] == 3):
					return 0
				elif(self.matrix[mx][my-1] == 4 or self.matrix[mx][my-1] == 5 or self.matrix[mx][my-1] == 6):
					return self.isNumberFull(mx,my-1)
				#Reviso si iluminar esa casilla altera algun numero que esta en la fila de arriba o de abajo o izquierda o derecha o una columna a la izquierda o una columna derecha
				up = self.checkUp(mx,my)
				down = self.checkDown(mx,my)
				rightcol = self.checkRightCol(mx,my)
				leftcol = self.checkLeftCol(mx,my)
				right = self.checkRight(mx,my)
				left = self.checkLeft(mx,my)
				if (up and down and right and left and rightcol and leftcol):
					return 1
				#Como se revisa primero si se puede quedar blanca y ahora se revisa que se pueda poner bombillo y no se puede ningua toca devolverse
				else:
					return -2
			#Como no la puedo modificar sigo adelante
			elif(self.matrix[mx][my] > 0):
				return -1
			
		else:
			if(self.matrix[mx][my] == 0 or self.matrix[mx][my] == 1):
				#Reviso si hay un numero alrededor y si dejandola sin bombillo esta puede alcanzar el numero necesario de bombillos
				if(self.matrix[mx+1][my] == 3):
					return 1
				elif(self.matrix[mx+1][my] == 7):
					return 0				
				elif(self.matrix[mx+1][my] == 4 or self.matrix[mx+1][my] == 5 or self.matrix[mx+1][my] == 6):
					return self.checkNumber(mx+1,my)
					
				if(self.matrix[mx-1][my] == 3):
					return 1
				elif(self.matrix[mx+1][my] == 7):
					return 0
				elif(self.matrix[mx-1][my] == 4 or self.matrix[mx-1][my] == 5 or self.matrix[mx-1][my] == 6):
					return self.checkNumber(mx-1,my)
				
				if(self.matrix[mx][my+1] == 3):
					return 1
				elif(self.matrix[mx+1][my] == 7):
					return 0
				elif(self.matrix[mx][my+1] == 4 or self.matrix[mx][my+1] == 5 or self.matrix[mx][my+1] == 6):
					return self.checkNumber(mx,my+1)
									
				if(self.matrix[mx][my-1] == 3):
					return 1
				elif(self.matrix[mx+1][my] == 7):
					return 0
				elif(self.matrix[mx][my-1] == 4 or self.matrix[mx][my-1] == 5 or self.matrix[mx][my-1] == 6):
					return self.checkNumber(mx,my-1)	
				#Como no hay ningun numero lo podemos quitar y devolvernos
				if(self.matrix[mx][my] == 1):
					return -2
				#Reviso si no esta iluminado y esta en la ultima fila y puede ser un bombillo, si no puede se devuelve			
				if(mx == self.x and self.matrix[mx][my] == 0 and self.functionB(1,mx,my) == 1):
					return 0
				else:
					return -2
				#Reviso si la posicion de arriba esta iluminada y si puede ser bombillo, si no puede se devuelve porque falta iluminación
				if(self.check(mx,my) == 0 and self.functionB(1,mx,my) == 1):
					return 0
				else:
					return -2
			else:
				return -1		
			
				

	def iluminate(self, mx, my):
		self.matrix[mx][my] = 1
		# mark with 9 up
		for x in range(mx,-1,-1):
			if self.matrix[x][my] >= 2 and self.matrix[x][my] <= 7:
				break
			if self.matrix[x][my] == 0 or self.matrix[x][my] == 8:
				self.matrix[x][my] = 9
		# mark with 9 down
		for x in range(mx, self.x):
			if self.matrix[x][my] >= 2 and self.matrix[x][my] <= 7:
				break
			if self.matrix[x][my] == 0 or self.matrix[x][my] == 8:
				self.matrix[x][my] = 9
		# mark with 9 left
		for y in range(my,-1,-1):
			if self.matrix[mx][y] >= 2 and self.matrix[mx][y] <= 7:
				break
			if self.matrix[mx][y] == 0 or self.matrix[mx][y] == 8:
				self.matrix[mx][y] = 9
		# mark with 9 right
		for y in range(my, self.y):
			if self.matrix[mx][y] >= 2 and self.matrix[mx][y] <= 7:
				break
			if self.matrix[mx][y] == 0 or self.matrix[mx][y] == 8:
				self.matrix[mx][y] = 9

	def checkOtherIlumination(self,mx,my,bx,by):
		# check if there are another bulb before the iluminated block up
		for x in range(mx,-1,-1):
			if self.matrix[x][my] >= 2 and self.matrix[x][my] <= 7:
				break
			if self.matrix[x][my] == 1 and x != bx:
				return True
		# check if there are another bulb after the iluminated block down
		for x in range(mx, self.x):
			if self.matrix[x][my] >= 2 and self.matrix[x][my] <= 7:
				break
			if self.matrix[x][my] ==  1 and x != bx:
				return True
		# check if there are another bulb after the iluminated block left
		for y in range(my,-1,-1):
			if self.matrix[mx][y] >= 2 and self.matrix[mx][y] <= 7:
				break
			if self.matrix[mx][y] == 1 and y != by:
				return True
		# check if there are another bulb after the iluminated block right
		for y in range(my, self.y):
			if self.matrix[mx][y] >= 2 and self.matrix[mx][y] <= 7:
				break
			if self.matrix[mx][y] == 1 and y != by:
				return True
		return False
			
		
	
	def deIluminate(self, mx, my):
		self.matrix[mx][my] = 0
		# mark with 0 up
		for x in range(mx,-1,-1):
			if self.matrix[x][my] >= 2 and self.matrix[x][my] <= 7:
				break
			if self.matrix[x][my] == 9 and self.checkOtherIlumination(x,my,mx,my):
				self.matrix[x][my] = 0
		# mark with 0 down
		for x in range(mx, self.x):
			if self.matrix[x][my] >= 2 and self.matrix[x][my] <= 7:
				break
			if self.matrix[x][my] == 9 and self.checkOtherIlumination(x,my,mx,my):
				self.matrix[x][my] = 0
		# mark with 0 left
		for y in range(my,-1,-1):
			if self.matrix[mx][y] >= 2 and self.matrix[mx][y] <= 7:
				break
			if self.matrix[mx][y] == 9 and self.checkOtherIlumination(mx,y,mx,my):
				self.matrix[mx][y] = 0
		# mark with 0 right
		for y in range(my, self.y):
			if self.matrix[mx][y] >= 2 and self.matrix[mx][y] <= 7:
				break
			if self.matrix[mx][y] == 9 and self.checkOtherIlumination(mx,y,mx,my):
				self.matrix[mx][y] = 0
				
	def backtracking(self):
		dir = 1
		x = y = 0
		while(x < self.x):
			y = 0
			while(y < self.y):
				opciones = self.functionT(x,y,dir)
				for valor in opciones:
					res = self.functionB(valor,x,y)
					if(res == 1 and valor == 1):
						self.iluminate(x,y)
						y += 1				
						dir = 1		
						break
					if(res == 1 and valor == 0 and self.matrix[x][y] == 1):
						self.deIluminate(x,y)
						y -= 1
						break
					if(res == 0):
						continue
					if(res == -1 and dir == 1):
						y += 1
						break
					if(res == -1 and dir == -1):
						y -= 1
						break
					if(res == -2):
						dir = -1
						y -= 1
						break
					if(y < 0):
						x -= 1
						break
				if(y < 0):
					break
			x+=1
	def printMatrix(self,text):
		print ("")
		print ("=================["+text+"]=====================")
		print ("")
		for row in self.matrix:
			print (row)
			
backtrack = AkariBacktracking()
backtrack.printMatrix("Input")
backtrack.backtracking()
backtrack.printMatrix("Result")
