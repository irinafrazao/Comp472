# Team Members:
# Zach Eichler 40018021
# Irina Patrocinio-Frazao 40024714
# Emilie Mines 40045370

class Node:
    
    # parent: the whole parent node
    # indexes_move_1: tuple (row,col) of which puzzle piece we are moving
    # indexes_move_2: tuple (row,col) of which puzzle piece we are moving
    # state: the state of the node; taking the parent state and swapping both indexes_move
    # depth: depth in the tree where this node resides
    # grid_size: size of the board (i.e. 3x3 would be size=3)
    def __init__(self, parent, indexes_move_1, indexes_move_2, state, depth, grid_size):
        self.parent = parent
        self.indexes_move_1 = indexes_move_1
        self.indexes_move_2 = indexes_move_2
        self.state = state
        self.depth = depth
        self.grid_size = grid_size
        
    def print_node(self):
        print("parent: ", self.parent)
        print("indexes_move_1: ", self.indexes_move_1)
        print("indexes_move_2: ", self.indexes_move_2)
        print("state: ", self.state)
        print("depth: ", self.depth)
        print("size: ", self.grid_size)
        print("\n")
        