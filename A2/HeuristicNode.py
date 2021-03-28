# Team Members:
# Zach Eichler 40018021
# Irina Patrocinio-Frazao 40024714
# Emilie Mines 40045370

class HeuristicNode:
    def __init__(self, parent, indexes_move_1, indexes_move_2,state,depth,fval, grid_size):
        self.parent = parent
        self.indexes_move_1 = indexes_move_1
        self.indexes_move_2 = indexes_move_2
        self.state = state
        self.depth = depth
        self.fval = fval
        self.grid_size = grid_size
        
    def print_node(self):
        print("parent: ", self.parent)
        print("indexes_move_1: ", self.indexes_move_1)
        print("indexes_move_2: ", self.indexes_move_2)
        print("state: ", self.state)
        print("depth: ", self.depth)
        print("fval: ", self.fval)
        print("size: ", self.grid_size)
        print("\n")