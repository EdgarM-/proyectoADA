from tkinter import *
from backTrackAkari import *


class GuiAkari():
	"""docstring for GuiAkari"""
	def __init__(self,master):
		self.mainWindow = master
		self.mainWindow.title("Akari Solver SQ-EA")
		self.app = Frame(self.mainWindow)		
		self.app.grid()
		self.loadButton = Button(self.app, text="Abrir archivo",command=lambda: self.openFile())
		self.loadButton.grid()

	def openFile(self):
		filename = filedialog.askopenfilename(filetypes=(("Text files","*.txt"),("All files","*.*")))
		if(filename):
			self.backtrack = AkariBacktracking(filename)
			self.paint()
		else:
			print("No file selected")

	def paint(self):
		self.labels = []
		for x in range(self.backtrack.x):
			tmpLabels=[]
			for y in range(self.backtrack.y):
				tmp = Label(self.app,width=2,height=2)
				if(self.backtrack.matrix[x][y] == 0):
					tmp.config(bg="#FFFFFF")
				elif(self.backtrack.matrix[x][y] == 2):
					tmp.config(bg="#000000")
				elif(self.backtrack.matrix[x][y] > 2 and self.backtrack.matrix[x][y] < 8):
					tmp.config(bg="#000000",fg="#FFFFFF")
					tmp.config(text=str(self.backtrack.matrix[x][y]-3))
				elif(self.backtrack.matrix[x][y] == 9):
					tmp.config(bg="#FFFF00")
				else:
					tmp.config(bg="#FFFF00")
					tmp.config(text="○")
				tmpLabels.append(tmp)
				tmp.grid(row=x,column=y)
			self.labels.append(tmpLabels)
		self.FirstSolutionButton = Button(self.app, text="Algoritmo primera entrega",command=lambda: self.openFile())
		self.FirstSolutionBackButton = Button(self.app, text="Algoritmo primera entrega + Backtracking",command=lambda: self.openFile())
		self.backtrackingButton = Button(self.app, text="Backtracking",command=lambda: self.openFile())
		self.FirstSolutionButton.grid(row=1, column=y+2)
		self.FirstSolutionBackButton.grid(row=2, column=y+2)
		self.backtrackingButton.grid(row=3, column=y+2)
		self.loadButton.grid(row=4, column=y+2)
		
			
main = Tk()
gui = GuiAkari(main)
gui.mainWindow.mainloop()
