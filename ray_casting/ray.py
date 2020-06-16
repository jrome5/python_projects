import cv2
from math import cos, sin, radians, pow, sqrt
from vectors import Point, Vector

class Ray:
	def __init__(self, x, y, angle):
		self.pos = Vector(x,y,0)
		self.dir = self.angleToVector(angle)
		self.size = 10


	def angleToVector(self, angle):
		return Vector(cos(angle), sin(angle), 0)


	def show(self, canvas):
		start = self.pos
		end = Vector(self.pos.x + self.dir.x * self.size, self.pos.y + self.dir.y * self.size, 0)
		canvas = cv2.line(canvas, (int(start.x), int(start.y)), (int(end.x), int(end.y)), (255,255,255), 1)
	
	def cast(self, wall):
		x1 = wall.a.x;
		y1 = wall.a.y;
		x2 = wall.b.x;
		y2 = wall.b.y;

		x3 = self.pos.x;
		y3 = self.pos.y;
		x4 = self.pos.x + self.dir.x;
		y4 = self.pos.y + self.dir.y;

		den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4);
		if(den == 0):
			return None

		t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den;
		u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den;
		if ((t > 0) and (t < 1) and (u > 0)):
			pt = Vector(0,0,0)
			pt.x = x1 + t * (x2 - x1)
			pt.y = y1 + t * (y2 - y1)
			return pt
		else:
			return None;


	#def setAngle(self, angle):

	def lookAt(self, x, y):
		self.dir.x = x - self.pos.x
		self.dir.y = y - self.pos.y
		self.dir = normalise(self.dir)

def normalise(vector):
	mag = sqrt(pow(vector.x, 2) + pow(vector.y, 2))
	vector.x = vector.x / mag
	vector.y = vector.y / mag
	return vector
