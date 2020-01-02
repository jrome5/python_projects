
import sys

class Vertex:
    def __init__(self, node):
        self.x = 0
        self.y = 0
        self.id = node
        self.adjacent = {}
        self.visited = False
        self.distance = sys.maxint
        self.previous = None
        self.highlighted = False
        self.obstacle = False

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([i.id for i in self.adjacent])

    def set_position(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y

    def get_position(self):
        return self.x, self.y
        
    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_weight(self, neighbor, weight):
        self.adjacent[neighbor] = weight

    def set_visited(self):
        self.visited = True

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def get_previous(self):
        return self.previous

    def set_highlighted(self, state):
        self.highlighted = state

    def get_highlighted(self):
        return self.highlighted

    def set_obstacle(self):
        self.obstacle = True
        for next in self.adjacent:
          #set weights to infinite for all connections to this cell
          #making this cell unreachable
          self.set_weight(next, sys.maxint)

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, new_vertex):
        self.vert_dict[self.num_vertices] = new_vertex
        self.num_vertices = self.num_vertices + 1
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        try:
            self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
            self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)
        except:
            print("Attempted to add edge frm: %s to: %s" %(frm, to))

    def get_vertices(self):
        return self.vert_dict.keys()

    def printAllConnections(self):
        for v in self.vert_dict:
            for w in v.get_connections():
                vid = v.get_id()
                wid = w.get_id()
                print('( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w)))

    def getMovementDirection(self, frm_id, to_id):
        # if next ID is greater -> right or down, if next ID is smaller -> left or up
        movement = ""
        if(frm_id < to_id):
            if(frm_id == to_id - 1):
                movement =  "right"
            else:
                movement = "down"
        else:
            if(frm_id == to_id + 1):
                movement = "left"
            else:
                movement = "up"
        return movement


