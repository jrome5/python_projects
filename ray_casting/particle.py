import cv2
from math import pow, sqrt, radians, inf, atan2
from ray import Ray
from vectors import Point, Vector

class Particle:
	def __init__(self, sceneW, sceneH):
		self.fov = 90
		self.pos = Vector(sceneW / 2, sceneH/ 2, 0)
		self.rays = []
		self.heading = 0
		self.spacing = 5
		for a in range(int(-self.fov / 2), int(self.fov / 2), self.spacing):
			self.rays.append(Ray(self.pos.x, self.pos.y, radians(a)))

	def update(self, x, y):
		self.pos = Vector(x, y, 0)
		for ray in self.rays:
			ray.pos = self.pos

	def show(self, canvas):
		width = 4
		height = 4
		canvas = cv2.ellipse(canvas, (int(self.pos.x), int(self.pos.y)), (width, height), 0,0,360, (255,255,255),1)
		for ray in self.rays:
			ray.show(canvas)

	def distance(self, v1, v2):
		diff = pow((v1.x-v2.x),2) + pow((v1.y-v2.y),2)
		return sqrt(diff)

	def lookAt(self, walls, canvas):
		for ray in self.rays:
			closest = None
			record = inf
			for wall in walls:
				pt = ray.cast(wall)
				if(pt):
					d = self.distance(self.pos, pt)
					if(d < record):
						record = d
						closest = pt
			if(closest):
				canvas = cv2.line(canvas, (int(self.pos.x), int(self.pos.y)), (int(closest.x), int(closest.y)), (255,255,255), 1)

