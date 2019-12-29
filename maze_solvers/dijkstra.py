import pygame
import time
import random
from graph import *
import heapq

def shortest(v, path):
		''' make shortest path from v.previous'''
		if v.previous:
				path.append(v.previous.get_id())
				shortest(v.previous, path)
		return

import heapq

def dijkstra(graph, start, target):
		start_vertex = graph.get_vertex(start)
		target_vertex = graph.get_vertex(target)
		print('''Dijkstra's shortest path''')
		# Set the distance for the start node to zero 
		for v in graph:
			v.set_distance(sys.maxint) #infitiy
			v.set_previous(None)
		start_vertex.set_distance(0)
		# Put tuple pair into the priority queue
		unvisited_queue = [(v.get_distance(),v) for v in graph]
		heapq.heapify(unvisited_queue)

		while len(unvisited_queue):
				# Pops a vertex with the smallest distance 
				uv = heapq.heappop(unvisited_queue)
				current = uv[1]
				current.set_visited()

				#for next in v.adjacent:
				for next in current.adjacent:
						# if visited, skip
						if next.visited:
								continue
						new_dist = current.get_distance() + current.get_weight(next)
						
						if new_dist < next.get_distance():
								next.set_distance(new_dist)
								next.set_previous(current)
								print('updated : current = %s next = %s new_dist = %s' \
												%(current.get_id(), next.get_id(), next.get_distance()))
						else:
								print('not updated : current = %s next = %s new_dist = %s' \
												%(current.get_id(), next.get_id(), next.get_distance()))

				# Rebuild heap
				# 1. Pop every item
				while len(unvisited_queue):
						heapq.heappop(unvisited_queue)
				# 2. Put all vertices not visited into the queue
				unvisited_queue = [(v.get_distance(),v) for v in graph if not v.visited]
				heapq.heapify(unvisited_queue)
				path = [target]
				shortest(graph.get_vertex(target), path)
				print 'The shortest path : %s' %(path[::-1])
		