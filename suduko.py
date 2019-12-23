import numpy as np
from random import shuffle

def main():
	# print(checkGrid(grid))
	print(values_list)
	fillGrid(grid)
	printGrid(grid)
	removeNValues(grid, 40)
	print("")
	printGrid(grid)


def fillGrid(grid):
    #Find next empty cell
  for i in range(0,grid_size):
    row=i//grid_length
    col=i%grid_length
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

def removeNValues(grid, N):
	for i in range(N):
		cell_number = np.random.randint(0,grid_size)
		row = cell_number//grid_length
		column = cell_number%grid_length
		grid[row][column] = 0
	return


def printGrid(grid):
	for row in range(0,grid_length):
		if(row == 3 or row == 6):
			print(" - - - - - - - - - - - -")
		rowtext = ""
		for column in range(0,grid_length):
			if(column == 3 or column == 6):
				rowtext = rowtext + " | "
			rowtext = rowtext + " " + str(int(grid[row][column]))
		print(rowtext)
	return

def checkGridFull(grid):
  for row in range(0,grid_length):
      for col in range(0,grid_length):
        if grid[row][col]==0:
          return False
  return True 

grid_length = 9
grid_size = grid_length**2
values_list = np.arange(1,grid_length+1)
grid = np.zeros((grid_length, grid_length))

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