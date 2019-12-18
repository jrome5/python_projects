import numpy as np
from random import shuffle

def main():
	# print(checkGrid(grid))
	print(values_list)
	fillGrid(grid)
	printGrid(grid)


def fillGrid(grid):
    #Find next empty cell
  for i in range(0,81):
    row=i//9
    col=i%9
    if grid[row][col]==0:
      shuffle(values_list)      
      for value in values_list:
        #Check that this value has not already be used on this row
        if(checkIfSafe(grid, row, col, value)):
          grid[row][col]=value
          if checkGridFull(grid):
            return True
          else:
            if fillGrid(grid):
              return True
      break
  grid[row][col]=0             

def remove

def printGrid(grid):
	for row in range(0,9):
		if(row == 3 or row == 6):
			print(" - - - - - - - - - - - -")
		rowtext = ""
		for column in range(0,9):
			if(column == 3 or column == 6):
				rowtext = rowtext + " | "
			rowtext = rowtext + " " + str(int(grid[row][column]))
		print(rowtext)
	return

#A function to check if the grid is full
def checkGridFull(grid):
  for row in range(0,9):
      for col in range(0,9):
        if grid[row][col]==0:
          return False
  #We have a complete grid!  
  return True 

values_list = [1,2,3,4,5,6,7,8,9]
grid = np.zeros((9,9))

def checkIfSafe(grid, row, column, value):
	return (notUsedInRow(grid, row, value) and notUsedInColumn(grid, column, value) and notUsedInSquare(grid, row-row%3, column-column%3, value))

def notUsedInRow(grid, row, value):
	return not(value in grid[row])

def notUsedInColumn(grid, column, value):
	return not value in (grid[0][column],grid[1][column],grid[2][column],grid[3][column],grid[4][column],grid[5][column],grid[6][column],grid[7][column],grid[8][column])

def notUsedInSquare(grid, row_start, column_start, value):
	for i in range(0,3):
		for j in range(0,3):
			if(grid[row_start+i][column_start+j] == value):
				return False
	return True

if __name__ == '__main__':
	main()