import pygame
import time
import random

def makeGrid(grid, size):
  for row in range(size):
    for col in range(size):
      x = (col * w)+ padding
      y = (row * w) + padding
      pointslist = (x, y, w, w)
      pygame.draw.rect(screen, grey, pointslist)                               # inner cell
      pygame.draw.line(screen, dark_grey, [x, y], [x + w, y], thickness)           # top of cell
      pygame.draw.line(screen, dark_grey, [x + w, y], [x + w, y + w], thickness)   # right of cell
      pygame.draw.line(screen, dark_grey, [x + w, y + w], [x, y + w], thickness)   # bottom of cell
      pygame.draw.line(screen, dark_grey, [x, y + w], [x, y], thickness)           # left of cell
      grid.append((x,y))
  pygame.display.update()
  return grid

# def generateMaze(start_point = 10):
   # starting positing of maze
   # place starting cell into stack
   # add starting cell to visited list
   # loop until stack is empty
     # slow program now a bit
     # define cell list
     # right cell available?
      # if yes add to cell list
     # left cell available?
     # down cell available?
     # up cell available?
     # check to see if cell list is empty
     # select one of the cell randomly
     # if this cell has been chosen
       # call push_right function
       # solution = dictionary key = new cell, other = current c
       # make this cell the current cell
       # add to visited list
       # place current cell on to stack
     # if no cells are available pop one from the stack
       # use single_cell function to show backtracking image
       # slow program down a bit
       # change colour to green to identify backtracking path

def push_up(x, y):
    pygame.draw.rect(screen, blue, (x + 1, y - w + 1, w - thickness, (2*w)-thickness), 0)         # draw a rectangle twice the width of the cell

def push_down(x, y):
    pygame.draw.rect(screen, blue, (x +  1, y + 1, w-thickness, (2*w)-thickness), 0)

def push_left(x, y):
    pygame.draw.rect(screen, blue, (x - w +1, y +1, (2*w)-thickness, w - thickness), 0)


def push_right(x, y):
    pygame.draw.rect(screen, blue, (x +1, y +1, (2*w)-thickness, w - thickness), 0)


def single_cell( x, y):
    pygame.draw.rect(screen, red, (x +1, y +1, w-thickness-1, w-thickness-1), 0)          # draw a single width cell


def backtracking_cell(x, y):
    pygame.draw.rect(screen, blue, (x +1, y +1, w-thickness-1, w-thickness-1), 0)        # used to re-colour the path after single_cell


def generateMaze(start_point, size, animate=True):
    delay = 0.1/(size**2) if animate else 0 
    x = start_point
    y = start_point
    single_cell(x, y)                                              # starting positing of maze
    stack.append((x,y))                                            # place starting cell into stack
    visited.append((x,y))                                          # add starting cell to visited list
    while len(stack) > 0:                                          # loop until stack is empty
        time.sleep(delay)                                            # slow program now a bit
        cell = []                                                  # define cell list
        cell_right = (x + w, y)
        if cell_right not in visited and cell_right in grid:       # right cell available?
            cell.append("right")                                   # if yes add to cell list

        cell_left = (x - w, y)
        if cell_left not in visited and cell_left in grid:       # left cell available?
            cell.append("left")

        cell_above = (x, y + w)
        if cell_above not in visited and cell_above in grid:     # down cell available?
            cell.append("down")

        cell_below = (x, y - w)
        if cell_below not in visited and cell_below in grid:      # up cell available?
            cell.append("up")

        if len(cell) > 0:                                          # check to see if cell list is empty
            cell_chosen = (random.choice(cell))                    # select one of the cell randomly

            if cell_chosen == "right":                             # if this cell has been chosen
                push_right(x, y)                                   # call push_right function
                x = x + w                                          # make this cell the current cell
                visited.append((x, y))                              # add to visited list
                stack.append((x, y))                                # place current cell on to stack

            elif cell_chosen == "left":
                push_left(x, y)
                x = x - w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "down":
                push_down(x, y)
                y = y + w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "up":
                push_up(x, y)
                y = y - w
                visited.append((x, y))
                stack.append((x, y))
            if animate:    
              pygame.display.update()
        else:
            x, y = stack.pop()                                    # if no cells are available pop one from the stack
            single_cell(x, y)                                     # use single_cell function to show backtracking image
            time.sleep(delay)                                       # slow program down a bit
            backtracking_cell(x, y)                               # change colour to green to identify backtracking path

width = 500
height = 500
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
black = [0,0,0]
grey = [150,150,150]
dark_grey = [50,50,50]
blue = [25,34,98]
red = [255, 50, 50]
font = pygame.font.SysFont(None, 48)
pygame.display.set_caption("Maze Generator")

grid = []
stack = []
visited = []
grid_size = 30
FPS = 30
padding = 10
thickness = 1
w = (width-(padding*2))/grid_size    
grid = makeGrid(grid, grid_size)
generateMaze(padding, grid_size, False)
pygame.display.update()

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
          running = False
        while event.type == pygame.KEYDOWN and event.key == pygame.K_p:
        	makeGrid()
pygame.quit()