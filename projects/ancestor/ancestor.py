from util import Stack 

class Graph:
    def __init__(self):
        self.vertices = {} 

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 not in self.vertices:
            self.add_vertex(v1)
        if v2 not in self.vertices:
            self.add_vertex(v2)
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v2].add(v1)
    
    # def dft(self, starting_vertex):
    #     # create an empty stack, push the starting vertex index
    #     s = Stack()
    #     s.push(starting_vertex)
    #     # create a set to store the visited vertices
    #     visitied = set()
    #     # create a new empty list 
    #     new_list = []
    #     # while stack is not empty (len greater than 0)
    #     while s.size() > 0:
    #         # pop the first vertex
    #         v = s.pop()
    #         # if that vertex has not been visitied 
    #         if v not in visitied:
    #             # mark as visited and print for debugging
    #             new_list.append(v)
    #             visitied.add(v)
    #             # print(v)
    #             # iterate through the child vertices of the current vertex
    #             for next_vertex in self.vertices[v]:
    #                 # push the next vertex
    #                 s.push(next_vertex)

    #     return new_list[-1]
    # check set  if empty = no ancestor: return -1
    # if ancestor return the lowest digit

    def dfs(self, starting_vertex):
        # Create an empty stack and push A PATH TO the starting vertex ID
        s = Stack()
        s.push([starting_vertex])

        # set a variable called longest path that stored the longest path we have
        longest_path = 1
        earliest_ancestor = -1

        # While the stack is not empty...
        while s.size() > 0:
            # pop the first PATH eg -> [a, b, c, r, g]
            path = s.pop()
            # Grab the last vertex from the PATH and store in current vertex variable
            current_vertex = path[-1]

            # now check if the lenth of our path is equal to the longes tpath 
            if len(path) == longest_path:
                # if so, check if the current vertex is smaller than the earliest ancestor 
                if current_vertex < earliest_ancestor:
                    # update the longest path to be the path we're on and the earliest ancestor to be the current vertex
                    longest_path = len(path)
                    earliest_ancestor = current_vertex

            # then check (if path is not equal to longest path)if the length of our path is greater than the longes tpath
            if len(path) > longest_path:
                # if so, update the longest path to be the path we're on and the earliest ancestor to be the current vertex
                longest_path = len(path)
                earliest_ancestor = current_vertex
            
            # For all of the ancestors acosiated with the current vertex
            for ancestor in self.vertices[current_vertex]:
                # copy the path that we used in order to get to this vertex
                new_path = list(path)
                # append the ancestor accosiated with the vertex to the new path
                new_path.append(ancestor)
                # Store the list in the Queue and reloop
                s.push(new_path)

        print(path)
        print(earliest_ancestor)
        # return the earliest_ancestor
        return earliest_ancestor
        


def earliest_ancestor(ancestors, starting_node):
    # This is a relationship graph
    # The data is formatted as a list of (parent, child) pairs. I.e (1, 3) --> 3 is a child of one, 3 is a child of 2. 6 is a child of 3, 6 is a child of 5 etc --> [(1,3), (2,3), (3,6), (5,6)]
    # We need to write a function that returns their earliest known ancestor, assuming that every step 'up' has the same weight. Therefore, whichever path has the most 'steps'/edges going up leads to the earliest known ancestor.

    # create a new graph
    graph = Graph()
    print('hello')
    
    # loop over ancestors and for each add a new edge as a pair (passing in the first and second)
    for ancestor in ancestors:
        parent = ancestor[0]
        child = ancestor[1]
        # graph.add_vertex(parent)
        # graph.add_vertex(child)
        graph.add_edge(parent, child)

    # then use the dfs function to traverse through the graph starting at the starting node and store in a variable traversed_graph
    traversed_graph = graph.dfs(starting_node)
    print(traversed_graph)
    # if there are no ancestors (if after traversing we're still at the beginning)

    if traversed_graph == starting_node:
        #  return -1
        return -1
    # loop over the stored path, get the smallest number
    # otherwise return the result of the traversal
    return traversed_graph 

