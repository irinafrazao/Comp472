# Team Members:
# Zach Eichler 40018021
# Irina Patrocinio-Frazao 40024714
# Emilie Mines 40045370

import enum

class Node:
    
    # parent: the whole parent node
    # direction: the direction we are moving the puzzle in this node (up, down, left, right)
    # index_move: tuple (col,row) of which puzzle piece we are moving
    # state: the state of the node; taking the parent state and moving the index_move in the direction
    # depth: depth in the tree where this node resides
    def __init__(self, parent, direction, index_move, state, depth):
        self.parent = parent
        self.direction = direction
        self.state = state
        self.index_move = index_move
        self.depth = depth
        
    def print_node(self):
        print("parent: ", self.parent)
        print("direction: ", self.direction)
        print("index_move: ", self.index_move)
        print("state: ", self.state)
        print("depth: ", self.depth)
        print("\n")
        
    def compare_equality_2_nodes(node1, node2):
    
        # get all values in tuple1 as a list
        values1 = [] 
        for t in node1.state:
            for value in t:
                values1.append(value)
                
        # get all values in tuple2 as a list
        values2 = [] 
        for t in node2.state:
            for value in t:
                values2.append(value)
        
        # ADD CHILDREN CHECK
        stateEquality = values1 == values2

        if stateEquality == True:
            return True
        else:
            return False
    
        
        
class Directions(enum.Enum):
   Up = 0
   Down = 1
   Left = 2
   Right = 3
        