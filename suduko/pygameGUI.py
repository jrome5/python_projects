import pygame
from generator import Suduko
import time

def generateSoduko():
	suduko = Suduko(9)
	suduko_text = suduko.printGridAsList()
	screen.fill((255, 255, 255))
	i = 0
	for row in suduko_text:
		text = font.render(row, True, black)
		screen.blit(text,(100, (i*text.get_height()) + 30))
		i = i + 1
		pygame.display.update()
		time.sleep(0.1)

width = 640
height = 480
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True
black = [0,0,0]
font = pygame.font.SysFont(None, 48)
text = font.render("Hello, World", True, black)
FPS = 30
screen.fill((255, 255, 255))
generateSoduko()


while running:
		clock.tick(30)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				running = False
			if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
				generateSoduko()
pygame.quit()