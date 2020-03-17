from util import Stack, Queue 

def earliest_ancestor(ancestors, starting_node):
    # This is a relationship graph
    # The data is formatted as a list of (parent, child) pairs. I.e (1, 3) --> 3 is a child of one, 3 is a child of 2. 6 is a child of 3, 6 is a child of 5 etc --> [(1,3), (2,3), (3,6), (5,6)]
    # We need to write a function that returns their earliest known ancestor,
    pass