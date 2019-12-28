import pygame
import time
import random
from graph import *

def makeGrid(screen, size, padding, width, thickness):
  grid = []
  graph = Graph()
  cell_id = 0
  for row in range(size):
    for col in range(size):
      x = (col * width)+ padding
      y = (row * width) + padding
      pointslist = (x, y, width, width)
      pygame.draw.rect(screen, grey, pointslist)                               # inner cell
      pygame.draw.line(screen, black, [x, y], [x + width, y], thickness)           # top of cell
      pygame.draw.line(screen, black, [x + width, y], [x + width, y + width], thickness)   # right of cell
      pygame.draw.line(screen, black, [x + width, y + width], [x, y + width], thickness)   # bottom of cell
      pygame.draw.line(screen, black, [x, y + width], [x, y], thickness)           # left of cell
      grid.append((x,y))
      cell = Vertex(cell_id)
      cell.set_position(x, y)
      graph.add_vertex(cell)
  pygame.display.update()
  return grid, graph


def generateMaze(screen, grid, graph, start_point, size, width, thickness, animate=True):
    stack = []
    cell_stack = []
    visited = []
    delay = 0.1/(size**2) if animate else 0 
    x = start_point
    y = start_point
    pygame.draw.rect(screen, red, (x +1, y +1, width-thickness-1, width-thickness-1), 0)          # draw a single width cell 
    stack.append((x,y))                                            # place starting cell into stack
    cell_stack.append(0)
    visited.append((x,y))                                          # add starting cell to visited list
    cell_id = 0
    while len(stack) > 0:                                          # loop until stack is empty
        time.sleep(delay)                                            # slow program now a bit
        cell = []                                                  # define cell list
        cell_right = (x + width, y)
        if cell_right not in visited and cell_right in grid:       # right cell available?
            cell.append("right")                                   # if yes add to cell list

        cell_left = (x - width, y)
        if cell_left not in visited and cell_left in grid:       # left cell available?
            cell.append("left")

        cell_above = (x, y + width)
        if cell_above not in visited and cell_above in grid:     # down cell available?
            cell.append("down")

        cell_below = (x, y - width)
        if cell_below not in visited and cell_below in grid:      # up cell available?
            cell.append("up")

        cell_chosen_id = 0
        if len(cell) > 0:                                          # check to see if cell list is empty
            cell_chosen = (random.choice(cell))                    # select one of the cell randomly
            if cell_chosen == "right":                             # if this cell has been chosen
                pygame.draw.rect(screen, blue, (x +1, y +1, (2*width)-thickness, width - thickness), 0)
                cell_chosen_id = cell_id + 1
                x = x + width                                          # make this cell the current cell
                visited.append((x, y))                              # add to visited list
                stack.append((x, y))                                # place current cell on to stack

            elif cell_chosen == "left":
                pygame.draw.rect(screen, blue, (x - width +1, y +1, (2*width)-thickness, width - thickness), 0)
                cell_chosen_id = cell_id - 1
                x = x - width
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "down":
                pygame.draw.rect(screen, blue, (x +  1, y + 1, width-thickness, (2*width)-thickness), 0)
                cell_chosen_id = cell_id + size
                y = y + width
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "up":
                # draw a rectangle twice the width of the cell
                pygame.draw.rect(screen, blue, (x + 1, y - width + 1, width - thickness, (2*width)-thickness), 0)         
                cell_chosen_id = cell_id - size
                y = y - width
                visited.append((x, y))
                stack.append((x, y))

            graph.add_edge(cell_id, cell_chosen_id, 1)
            cell_id = cell_chosen_id
            cell_stack.append(cell_chosen_id)
            if animate:    
              pygame.display.update()
        else:
            x, y = stack.pop()                                    # if no cells are available pop one from the stack
            cell_id = cell_stack.pop()
            pygame.draw.rect(screen, red, (x +1, y +1, width-thickness-1, width-thickness-1), 0)          # draw a single width cell 
            time.sleep(delay)                                       # slow program down a bit
            pygame.draw.rect(screen, blue, (x +1, y +1, width-thickness-1, width-thickness-1), 0)        # used to re-colour the path after single_cell

#GUI colors
black = [0,0,0]
grey = [150,150,150]
blue = [25,34,98]
red = [255, 50, 50]


def main():
    width = 500
    height = 500
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 48)
    pygame.display.set_caption("Maze Generator")

    grid_size = 30
    FPS = 30
    padding = 10
    cell_thickness = 1
    cell_width = (width-(padding*2))/grid_size

    grid, graph = makeGrid(screen, grid_size, padding, cell_width, cell_thickness)
    generateMaze(screen, grid, graph, padding, grid_size, cell_width, cell_thickness, False)
    pygame.display.update()

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
              running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                print("New maze coming right up!")
                grid, graph = makeGrid(screen, grid_size, padding, cell_width, cell_thickness)
                generateMaze(screen, grid, graph, padding, grid_size, cell_width, cell_thickness, True)
        pygame.display.update()
    pygame.quit()

if __name__ == '__main__':
    main()
