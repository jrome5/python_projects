import pygame
import time
import random
from graph import *
from dijkstra import *
from config import simConfig

def makeGrid(screen, config):
  size = config.getGridSize()
  width = config.getCellWidth()
  padding = config.getPadding()
  thickness = config.getCellThickness()
  grid = []
  graph = Graph()
  cell_id = 0
  for row in range(size):
    for col in range(size):
      x = (col * width)+ padding
      y = (row * width) + padding
      pointslist = (x, y, width, width)
      pygame.draw.rect(screen, config.getGreyColor(), pointslist)                               # inner cell
      pygame.draw.line(screen, config.getBlackColor(), [x, y], [x + width, y], thickness)           # top of cell
      pygame.draw.line(screen, config.getBlackColor(), [x + width, y], [x + width, y + width], thickness)   # right of cell
      pygame.draw.line(screen, config.getBlackColor(), [x + width, y + width], [x, y + width], thickness)   # bottom of cell
      pygame.draw.line(screen, config.getBlackColor(), [x, y + width], [x, y], thickness)           # left of cell
      grid.append((x,y))
      cell = Vertex(cell_id)
      cell.set_position(x, y)
      graph.add_vertex(cell)
      cell_id = cell_id + 1
  pygame.display.update()
  return grid, graph


def generateMaze(screen, grid, graph, config, animate=True):
    size = config.getGridSize()
    width = config.getCellWidth()
    padding = config.getPadding()
    thickness = config.getCellThickness()
    stack = []
    cell_stack = []
    visited = []
    delay = config.getSimDelay(animate)
    x = config.getPadding()
    y = config.getPadding()
    if animate:
      config.drawSingleWidthCell(screen, x, y, config.getRedColor())
      pygame.display.update()
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
                cell_chosen_id = cell_id + 1

            elif cell_chosen == "left":
                cell_chosen_id = cell_id - 1

            elif cell_chosen == "down":
                cell_chosen_id = cell_id + size

            elif cell_chosen == "up":
                cell_chosen_id = cell_id - size

            config.moveMarker(screen, x, y, cell_chosen, config.getBlueColor())         
            x, y = config.moveCoords(x,y, cell_chosen)          # make this cell the current cell
            visited.append((x, y))                              # add to visited list
            stack.append((x, y))                                # place current cell on to stack
            graph.add_edge(cell_id, cell_chosen_id, 1)
            cell_id = cell_chosen_id
            cell_stack.append(cell_chosen_id)
            if animate:    
              pygame.display.update()
        else:
            x, y = stack.pop()                                    # if no cells are available pop one from the stack
            cell_id = cell_stack.pop()
            pygame.draw.rect(screen, config.getRedColor(), (x +1, y +1, width-thickness-1, width-thickness-1), 0)          # draw a single width cell 
            if animate:    
              pygame.display.update()
            time.sleep(delay)                                       # slow program down a bit
            pygame.draw.rect(screen, config.getBlueColor(), (x +1, y +1, width-thickness-1, width-thickness-1), 0)        # used to re-colour the path after single_cell
            if animate:    
              pygame.display.update()

def printOpeningMessage():
    opening_message = "Welcome"
    controls_message = "Press \'M\' to generate a new maze, press \'D\' to solve this with Dijkstra algorithm and press \'Esc\' to quit"
    print(opening_message + '\n' + controls_message)
    return

def main():
    pygame.init()
    sim_config = simConfig()
    screen = pygame.display.set_mode((sim_config.getWidth(), sim_config.getHeight()))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 48)
    pygame.display.set_caption("Maze Generator")

    grid, graph = makeGrid(screen, sim_config)
    generateMaze(screen, grid, graph, sim_config, False)
    pygame.display.update()
    printOpeningMessage()
    running = True
    while running:
        clock.tick(sim_config.getFPS())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
              running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                print("New maze coming right up!")
                grid, graph = makeGrid(screen, sim_config)
                generateMaze(screen, grid, graph, sim_config, True)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                dijkstra(screen, graph, sim_config) #get from start to end
                time.sleep(1)
        pygame.display.update()
    pygame.quit()

if __name__ == '__main__':
    main()
