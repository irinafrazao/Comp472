# -*- coding: utf-8 -*-

class HeuristicNode:
    def __init__(self, parent, indexes_move_1, indexes_move_2,state,depth,fval, grid_size):
        self.parent = parent
        self.indexes_move_1 = indexes_move_1
        self.indexes_move_2 = indexes_move_2
        self.state = state
        self.depth = depth
        self.fval = fval
        self.grid_size = grid_size