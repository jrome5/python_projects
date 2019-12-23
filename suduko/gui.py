from tkinter import *
from generator import Suduko

root = Tk()
labels = []

def main():
	button  = Button(root, text = "Generate Suduko",command=generate)
	button.pack()
	root.mainloop()

def generate():
	suduko = Suduko(9)
	suduko.removeNValues(40)
	viewGrid(suduko)

def viewGrid(suduko):
	grid = Label(root, text=suduko.printGrid())
	grid.pack()
	# length = suduko.length
	# grid = suduko.grid
	# for row in range(length):
	# 	for col in range(length):
	# 		text = grid[row][col]
	# 		label = Label(root, text=text)
	# 		label.grid(row=row+1, column=col)
	# 		labels.append(label)


if __name__ == '__main__':
	main()