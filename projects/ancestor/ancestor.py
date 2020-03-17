from util import Stack 

class Graph:
    def __init__(self):
        self.vertices = {} 

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:    
            self.vertices[v1].add(v2)
        else: 
            raise IndexError("That vertex does not exist")
    
    def dft(self, starting_vertex):
        # create an empty stack, push the starting vertex index
        s = Stack()
        s.push(starting_vertex)
        # create a set to store the visited vertices
        visitied = set()
        # create a new empty list 
        new_list = []
        # while stack is not empty (len greater than 0)
        while s.size() > 0:
            # pop the first vertex
            v = s.pop()
            # if that vertex has not been visitied 
            if v not in visitied:
                # mark as visited and print for debugging
                new_list.append(v)
                visitied.add(v)
                print(v)
                # iterate through the child vertices of the current vertex
                for next_vertex in self.vertices[v]:
                    # push the next vertex
                    s.push(next_vertex)

        return new_list[-1]

def earliest_ancestor(ancestors, starting_node):
    # This is a relationship graph
    # The data is formatted as a list of (parent, child) pairs. I.e (1, 3) --> 3 is a child of one, 3 is a child of 2. 6 is a child of 3, 6 is a child of 5 etc --> [(1,3), (2,3), (3,6), (5,6)]
    # We need to write a function that returns their earliest known ancestor, assuming that every step 'up' has the same weight. Therefore, whichever path has the most 'steps'/edges going up leads to the earliest known ancestor.
    pass

