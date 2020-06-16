import cv2
import random
import sys
import numpy as np
from boundary import Boundary
from particle import Particle

sceneW = 480
sceneH = 640
mousePos = (0,0)
param = (0,0) #throwaway param
canvas =  np.zeros((sceneW, sceneH, 3), np.uint8)
walls = []
particle = Particle(sceneW, sceneH)

def setupWalls():
	for i in range(5):
		x1 = int(random.random() * sceneW)
		x2 = int(random.random() * sceneW)
		y1 = int(random.random() * sceneH)
		y2 = int(random.random() * sceneH)
		print("positions:%s,%s,%s,%s" %(x1,y1,x2,y2))
		wall = Boundary(x1,y1,x2,y2)
		walls.append(wall)
  
	walls.append(Boundary(0, 0, sceneH, 0))
	walls.append(Boundary(sceneH, 0, sceneH, sceneW))
	walls.append(Boundary(sceneH, sceneW, 0, sceneW))
	walls.append(Boundary(0, sceneW, 0, 0))

def showWalls(canvas):
	for wall in walls:
		wall.show(canvas)

# def drawRays():
# 	for i in range 
# 	ray = Ray(100, 200)
# 	ray.lookAt(mousePos[0],mousePos[1])
# 	ray.show(canvas)

# 	pt = ray.cast(wall)
# 	if(pt):
# 		width = 8
# 		height = 8
# 		canvas = cv2.ellipse(canvas, (int(pt.x), int(pt.y)), (width, height), 0,0,360, (255,255,255),1)


def main():
	#black canvas
	canvas =  np.zeros((sceneW, sceneH, 3), np.uint8)
	showWalls(canvas)
	particle.update(mousePos[0], mousePos[1])
	particle.lookAt(walls, canvas)
	# particle.show(canvas)
	# drawRays()
	# print("x%s, y%s" %(mousePos[0], mousePos[1]))
	cv2.imshow("Canvas", canvas)
	cv2.setMouseCallback("Canvas",mousePosition,param)

def mousePosition(event,x,y,flags,param):
		if event == cv2.EVENT_MOUSEMOVE:
				global mousePos
				mousePos = (x,y)

if __name__ == '__main__':
	setupWalls()
	while(1):
		main()
		k = cv2.waitKey(20)
		if((k == 27) or (k == ord('q'))): # wait for 'q' or ESC key to save and exit
			break
	cv2.destroyAllWindows()