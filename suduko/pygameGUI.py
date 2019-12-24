import pygame
from generator import Suduko
import time
width = 640
height = 480
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
done = False
running = True
black = [0,0,0]
font = pygame.font.SysFont(None, 32)
text = font.render("Hello, World", True, black)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
          running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
        	done = False
    
    i = 0
    if(not done):
    	suduko = Suduko(9)
    	suduko_text = suduko.printGridAsList()
    	screen.fill((255, 255, 255))
    	for row in suduko_text:
		    text = font.render(row, True, black)
		    screen.blit(text,(100, (i*text.get_height()) + 30))
		    i = i + 1
		    clock.tick(20)
		    pygame.display.update()
    	done = True
pygame.quit()