import cv2
from vectors import Point, Vector

class Boundary:
  def __init__(self, x1, y1, x2, y2):
  	self.a = Vector(x1, y1, 0);
  	self.b = Vector(x2, y2, 0);

  def show(self, canvas):
  	canvas = cv2.line(canvas, (self.a.x, self.a.y), (self.b.x, self.b.y), (255,255,255), 2)


