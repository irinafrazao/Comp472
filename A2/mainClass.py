# Team Members:
# Zach Eichler 40018021
# Irina Patrocinio-Frazao 40024714
# Emilie Mines 40045370

import DepthFirstSearch

initial_state = ((6,1,2),(7,8,3),(5,4,9))

# if we put limit to size exponent size, so it can complete bigger puzzles, falls into a subtree loop
size = len(initial_state)
limit = pow(size, size-1)

# cheat until we find why DPS goes into an infinite sub loop, use iterative deepening with high limit (size exponent size)
open_stack, closed_stack = DepthFirstSearch.depth_first_search(initial_state, True, limit) 



# Need to generate text outputs for each algorithms:
# solution output
# search output

# TODO: Analysis

# TODO: Scale up


