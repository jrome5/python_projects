class simConfig:
	def __init__(self):
		self.width = 500
		self.height = 500
		self.FPS = 30
		self.padding = 10
		self.grid_size = 4
		self.cell_thickness = 1
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
		return 0.1/(self.grid_size**2)

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