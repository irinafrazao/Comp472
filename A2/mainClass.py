# Team Members:
# Zach Eichler 40018021
# Irina Patrocinio-Frazao 40024714
# Emilie Mines 40045370

import UtilClass
import DepthFirstSearch
import IterativeDeepeningSearch


# example in assignment 6 moves
initial_state = ((9,8,7),(6,5,4),(3,2,1))

open_stack, closed_stack = IterativeDeepeningSearch.iterative_deepening_search(initial_state) 
search_path = UtilClass.get_search_path(closed_stack)
solution_path = UtilClass.get_solution_path(initial_state, closed_stack)

file = open("results.txt", "w")

file.write("Puzzle 1: " + str(initial_state) + "\n\n")
file.write("Iterative Deepening \n")

file.write("Solution path: \n")
file.write(str(solution_path) + "\n")
file.write("\n")

file.write("Search path: \n")
file.write(str(search_path) + "\n")
file.write("\n")

file.close()

#open_stack, closed_stack = DepthFirstSearch.depth_first_search(initial_state, False, limit) 
# TODO: fix DPS? never stops

#TODO: Add timer. (right now iterative deepening does a 4 move puzzle well in the 60 secs)
#TODO: Add 20 random puzzles as input

# TODO: heuristic 1
# TODO: heuristic 2

# TODO: Analysis

# TODO: Scale up


