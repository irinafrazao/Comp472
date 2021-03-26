# Team Members:
# Zach Eichler 40018021
# Irina Patrocinio-Frazao 40024714
# Emilie Mines 40045370

import UtilClass
from time import perf_counter
import DepthFirstSearch
import IterativeDeepeningSearch
import ManhattanDistance
import SumOfPermutations


class FNode:
    def __init__(node, g,h):
        node = node
        g =g
        h = h
    
    def get_F(node):
        return node.g+node.h

<<<<<<< Updated upstream
results = open("results.txt", "w")

# each line of file is one puzzle
inputs = open("inputs.txt", "r")

for index, initial_state in enumerate(inputs):
    results.write("Puzzle " + str(index + 1) + ": " + str(initial_state) + "\n")
    
    open_stack, closed_stack, computational_time = DepthFirstSearch.depth_first_search(initial_state, False, 0, perf_counter()) 
    search_path = UtilClass.get_search_path(initial_state, closed_stack)
    solution_path = UtilClass.get_solution_path(initial_state, closed_stack)
    
    results.write("Depth First Search => " + str(computational_time) + "secs \n")
    
    results.write("Solution path: \n")
    results.write(str(solution_path) + "\n")
    results.write("\n")

    results.write("Search path: \n")
    results.write(str(search_path) + "\n")
    results.write("\n")
    
    open_stack, closed_stack, computational_time = IterativeDeepeningSearch.iterative_deepening_search(initial_state) 
    search_path = UtilClass.get_search_path(initial_state, closed_stack)
    solution_path = UtilClass.get_solution_path(initial_state, closed_stack)

    results.write("Iterative Deepening => " + str(computational_time) + "secs \n")
    
    results.write("Solution path: \n")
    results.write(str(solution_path) + "\n")
    results.write("\n")

    results.write("Search path: \n")
    results.write(str(search_path) + "\n")
    results.write("\n")
    
    # TODO: heuristic 1 RESULTS
    # TODO: heuristic 2 RESULTS
    
    results.write("*********************************************************************************\n\n")

results.close()
inputs.close()
=======

# example in assignment 6 moves
initial_state = ((3,2,1),(6,5,4),(9,8,7))

#open_stack, closed_stack = IterativeDeepeningSearch.iterative_deepening_search(initial_state) 
#search_path = UtilClass.get_search_path(closed_stack)
#solution_path = UtilClass.get_solution_path(initial_state, closed_stack)

#file = open("results.txt", "w")

#file.write("Puzzle 1: " + str(initial_state) + "\n\n")
#file.write("Iterative Deepening \n")

#file.write("Solution path: \n")
#file.write(str(solution_path) + "\n")
#file.write("\n")

#file.write("Search path: \n")
#file.write(str(search_path) + "\n")
#file.write("\n")

#file.close()

#open_stack, closed_stack = DepthFirstSearch.depth_first_search(initial_state, False, limit) 
# TODO: fix DPS? never stops

#TODO: Add timer. (right now iterative deepening does a 4 move puzzle well in the 60 secs)
#TODO: Add 20 random puzzles as input

# TODO: heuristic 1

        
        

               
        
            
            
ManhattanDistance.manhattan_distance(initial_state)

SumOfPermutations.sum_of_permutations(initial_state)

        



# TODO: heuristic 2

# TODO: Analysis

# TODO: Scale up


>>>>>>> Stashed changes
