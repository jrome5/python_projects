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
        if not(value in grid[row]):
          #Check that this value has not already be used on this column
          if not value in (grid[0][col],grid[1][col],grid[2][col],grid[3][col],grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]):
            #Identify which of the 9 squares we are working on
            square=[]
            if row<3:
              if col<3:
                square=[grid[i][0:3] for i in range(0,3)]
              elif col<6:
                square=[grid[i][3:6] for i in range(0,3)]
              else:  
                square=[grid[i][6:9] for i in range(0,3)]
            elif row<6:
              if col<3:
                square=[grid[i][0:3] for i in range(3,6)]
              elif col<6:
                square=[grid[i][3:6] for i in range(3,6)]
              else:  
                square=[grid[i][6:9] for i in range(3,6)]
            else:
              if col<3:
                square=[grid[i][0:3] for i in range(6,9)]
              elif col<6:
                square=[grid[i][3:6] for i in range(6,9)]
              else:  
                square=[grid[i][6:9] for i in range(6,9)]
            #Check that this value has not already be used on this 3x3 square
            if not value in (square[0] + square[1] + square[2]):
              grid[row][col]=value
              if checkGridFull(grid):
                return True
              else:
                if fillGrid(grid):
                  return True
      break
  grid[row][col]=0             

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
grid = []
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

print(values_list)
fillGrid(grid)
printGrid(grid)
def getSquare(grid, row, column):
	#Identify which of the 9 squares we are working on
    square=[]
    c = column % 3
    if row<3:
        square=[grid[i][c:c+3] for i in range(0,3)]
    elif row<6:
        square=[grid[i][c:c+3] for i in range(0,3)]
    else:
        square=[grid[i][c:c+3] for i in range(0,3)]
    return square

# if __name__ == '__main__':
# 	main()