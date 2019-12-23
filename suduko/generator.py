import numpy as np
from random import shuffle

class Suduko:

	def __init__(self, length= 9):
		self.length = length
		self.size = self.length**2
		self.values_list = np.arange(1,self.length+1)
		self.grid = np.zeros((self.length, self.length))

		self.fillGrid();

	def fillGrid(self):
	    #Find next empty cell
	  for i in range(0,self.size):
	    row=i//self.length
	    col=i%self.length
	    if self.grid[row][col]==0:
	      shuffle(self.values_list)      
	      for value in self.values_list:
	        #Check that this value has not already be used on this row
	        if(self.checkIfSafe(row, col, value)):
	          self.grid[row][col]=value
	          if self.checkGridFull():
	            return True
	          else:
	            if self.fillGrid():
	              return True
	      break
	  self.grid[row][col]=0             

	def removeNValues(self, N):
		for i in range(N):
			cell_number = np.random.randint(0,self.size)
			row = cell_number//self.length
			column = cell_number%self.length
			self.grid[row][column] = 0
		return


	def printGrid(self):
		output = ""
		for row in range(0,self.length):
			if(row == 3 or row == 6):
				output = output + ("\n- - - - - - - - - - - -")
			rowtext = ""
			for column in range(0,self.length):
				if(column == 3 or column == 6):
					rowtext = rowtext + " | "
				rowtext = rowtext + " " + str(int(self.grid[row][column]))
			output = output + "\n" + rowtext
		return output

	def checkGridFull(self):
	  for row in range(0,self.length):
	      for col in range(0,self.length):
	        if self.grid[row][col]==0:
	          return False
	  return True 

	def checkIfSafe(self, row, column, value):
		return (self.notUsedInRow(row, value) and self.notUsedInColumn(column, value) and self.notUsedInSquare(row-row%3, column-column%3, value))

	def notUsedInRow(self, row, value):
		return not(value in self.grid[row])

	def notUsedInColumn(self, column, value):
		return not value in (self.grid[0][column],self.grid[1][column],self.grid[2][column],self.grid[3][column],self.grid[4][column],self.grid[5][column],self.grid[6][column],self.grid[7][column],self.grid[8][column])

	def notUsedInSquare(self, row_start, column_start, value):
		for i in range(0,3):
			for j in range(0,3):
				if(self.grid[row_start+i][column_start+j] == value):
					return False
		return True