import pygame

class simConfig:
	def __init__(self):
		self.width = 500
		self.height = 500
		self.FPS = 30
		self.padding = 10
		self.grid_size = 15
		self.cell_thickness = 3
		self.cell_width = self.calculateCellWidth()
		self.delay = self.calculateSimDelay()

	def getWidth(self):
		return self.width

	def getHeight(self):
		return self.height

	def getFPS(self):
		return self.FPS

	def getPadding(self):
		return self.padding

	def getGridSize(self):
		return self.grid_size

	def getCellThickness(self):
		return self.cell_thickness

	def getCellWidth(self):
		return self.cell_width

	def calculateCellWidth(self):
		return (self.width-(self.padding*2))/self.grid_size

	def calculateSimDelay(self, animate = True):
		return 1.0/(self.grid_size**2)

	def getSimDelay(self, animate=True):
		return self.delay if animate else 0

	def getBlackColor(self):
		return [0, 0, 0]

	def getGreyColor(self):
		return [150, 150, 150]

	def getBlueColor(self):
		return [25, 34, 98]

	def getRedColor(self):
		return [255, 50, 50]

	def getGreenColor(self):
		return [50, 255, 50]

	def moveUp(self, screen, x, y, color, cell_padding = 0):
		thickness = self.cell_thickness + cell_padding
		pygame.draw.rect(screen, color, (x + 1, y + 1 - self.cell_width, self.cell_width -thickness, (2*self.cell_width)-thickness), 0) 
		# draw a rectangle twice the cell_width of the cell

	def moveDown(self, screen, x, y, color, cell_padding = 0):
		thickness = self.cell_thickness + cell_padding
		pygame.draw.rect(screen, color, (x +  1, y + 1, self.cell_width -thickness, (2*self.cell_width)-thickness), 0)

	def moveLeft(self, screen, x, y, color, cell_padding = 0):
		thickness = self.cell_thickness + cell_padding
		pygame.draw.rect(screen, color, (x - self.cell_width + 1, y + 1, (2*self.cell_width)-thickness, self.cell_width -thickness), 0)

	def moveRight(self, screen, x, y, color, cell_padding = 0):
		thickness = self.cell_thickness + cell_padding	
		pygame.draw.rect(screen, color, (x + 1, y + 1, (2*self.cell_width)-thickness, self.cell_width -thickness), 0)

	def drawSingleWidthCell(self, screen, x, y, color):
		width = self.cell_width-1
		thickness = self.cell_thickness
		pygame.draw.rect(screen, color, (x + thickness+2, y + thickness+2, width-thickness-4, width-thickness-4), 0)          # draw a single width cell 

	def moveCoords(self, x, y, movement):
		if movement == "right":                      
			new_x = x + self.cell_width
			return new_x, y                     

		elif movement == "left":
			new_x = x - self.cell_width
			return new_x, y

		elif movement == "down":
			new_y = y + self.cell_width
			return x, new_y

		elif movement == "up":
			new_y = y - self.cell_width
			return x, new_y

	def moveMarker(self, screen, x, y, movement, color, cell_padding=0):
		if movement == "right":
			self.moveRight(screen, x, y, color, cell_padding)
		if movement == "left":
			self.moveLeft(screen, x, y, color, cell_padding)
		if movement == "down":
			self.moveDown(screen, x, y, color, cell_padding)
		if movement == "up":
			self.moveUp(screen, x, y, color, cell_padding)