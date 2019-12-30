import pygame
import time
import random
from graph import *
import heapq

def shortest(v, path):
		''' make shortest path from v.previous'''
		if v.previous:
				path.append(v.previous)
				shortest(v.previous, path)
		return

import heapq

def dijkstra(screen, graph, config):
		#get config parameters
		size = config.getGridSize()
		width = config.getCellWidth()
		padding = config.getPadding()
		thickness = config.getCellThickness()
		delay = config.getSimDelay()
		start = 0
		target = size**2 -1
		start_vertex = graph.get_vertex(start)
		target_vertex = graph.get_vertex(target)

		x, y = start_vertex.get_position()

		# draw a start and target cells
		config.drawSingleWidthCell(screen, x, y, config.getRedColor())
		target_x = padding + (size-1)*(width) + (width)/2
		target_y = target_x
		pygame.draw.circle(screen, config.getRedColor(), (target_x, target_y), (width-thickness*4)/2, 0) 
		pygame.display.update()

		print('''Dijkstra's shortest path''')
		# Set the distance for the start node to zero 
		for v in graph:
			v.set_distance(sys.maxint) #infitiy
			v.set_previous(None)
		start_vertex.set_distance(0)
		# Put tuple pair into the priority queue
		unvisited_queue = [(v.get_distance(),v) for v in graph]
		heapq.heapify(unvisited_queue)

		found_target = False
		while(len(unvisited_queue) and found_target == False):
				# Pops a vertex with the smallest distance 
				uv = heapq.heappop(unvisited_queue)
				current = uv[1]
				current.set_visited()
				x, y = current.get_position()
				time.sleep(delay)
				config.drawSingleWidthCell(screen, x, y, config.getRedColor())
				pygame.display.update()
				time.sleep(delay)

				#for next in v.adjacent:
				for next in current.adjacent:
						movement = graph.getMovementDirection(current.get_id(), next.get_id())
						config.moveMarker(screen, x, y, movement, config.getGreenColor())
						pygame.display.update()
						# if visited, skip
						if next.visited:
								continue
						new_dist = current.get_distance() + current.get_weight(next)
						
						if new_dist < next.get_distance():
							next.set_distance(new_dist)
							next.set_previous(current)
							config.drawSingleWidthCell(screen, x, y, config.getRedColor())
							pygame.display.update()
							time.sleep(delay)
					
				if(current.get_id() == target):
					found_target = True
				# Rebuild heap
				# 1. Pop every item
				while len(unvisited_queue):
						heapq.heappop(unvisited_queue)
				# 2. Put all vertices not visited into the queue
				unvisited_queue = [(v.get_distance(),v) for v in graph if not v.visited]
				heapq.heapify(unvisited_queue)
		path = [graph.get_vertex(target)]
		shortest(graph.get_vertex(target), path)
		print 'The shortest path : %s' %[v.get_id() for v in path[::-1]]
		path = path[::-1]
		drawPath(screen, path, graph, config)

def drawPath(screen, path, graph, config):
	delay = config.getSimDelay(True)
	x = y = config.getPadding()
	thickness = config.getCellThickness()
	for i in range(len(path)-1):
		current = path[i]
		next_v = path[i+1]
		movement = graph.getMovementDirection(current.get_id(), next_v.get_id())
		config.moveMarker(screen, x, y, movement, config.getRedColor(), thickness)
		x, y = config.moveCoords(x, y, movement)
		pygame.display.update()
		time.sleep(delay)