import pygame
import time

def makeGrid(grid, size, world_width, padding = 10):
  thickness = 1
  w = (world_width-(padding*2))/size
  for row in range(size):
    for col in range(size):
      x = (col * w)+ padding
      y = (row * w) + padding
      pointslist = (x, y, w, w)
      pygame.draw.rect(screen, grey, pointslist)                               # inner cell
      pygame.draw.line(screen, white, [x, y], [x + w, y], thickness)           # top of cell
      pygame.draw.line(screen, white, [x + w, y], [x + w, y + w], thickness)   # right of cell
      pygame.draw.line(screen, white, [x + w, y + w], [x, y + w], thickness)   # bottom of cell
      pygame.draw.line(screen, white, [x, y + w], [x, y], thickness)           # left of cell
      grid.append((x,y))
      delay = 1/(size**2)
      time.sleep(delay)
      pygame.display.update()
  return grid

width = 500
height = 500
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
black = [0,0,0]
grey = [150,150,150]
white = [255,255,255]
font = pygame.font.SysFont(None, 48)
pygame.display.set_caption("Maze Generator")
grid = []
grid_size = 10
FPS = 30
grid = makeGrid(grid, grid_size, width)

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