# Team Members:
# Zach Eichler 40018021
# Irina Patrocinio-Frazao 40024714
# Emilie Mines 40045370

import UtilClass
from time import perf_counter
import DepthFirstSearch
import IterativeDeepeningSearch
import AstarAlgorithm


results = open("results.txt", "w")

# each line of file is one puzzle
inputs = open("inputs.txt", "r")

for index, initial_state in enumerate(inputs):

    # turn string from input into a python obj (tuple of tuple)
    initial_state = eval(initial_state)    

    results.write("Puzzle " + str(index + 1) + ": " + str(initial_state) + "\n")
    
    open_stack, closed_stack, computational_time = DepthFirstSearch.depth_first_search(initial_state, False, 0, perf_counter()) 
    search_path = UtilClass.get_search_path(initial_state, closed_stack)
    solution_path = UtilClass.get_solution_path(initial_state, closed_stack)
    
    results.write("DEPTH FIRST SEARCH => " + str(computational_time) + "secs \n")
    
    results.write("Solution path: \n")
    results.write(str(solution_path) + "\n")
    results.write("\n")

    results.write("Search path: \n")
    results.write(str(search_path) + "\n")
    results.write("\n")
    
    open_stack, closed_stack, computational_time = IterativeDeepeningSearch.iterative_deepening_search(initial_state) 
    search_path = UtilClass.get_search_path(initial_state, closed_stack)
    solution_path = UtilClass.get_solution_path(initial_state, closed_stack)

    results.write("ITERATIVE DEEPENING => " + str(computational_time) + "secs \n")
    
    results.write("Solution path: \n")
    results.write(str(solution_path) + "\n")
    results.write("\n")

    results.write("Search path: \n")
    results.write(str(search_path) + "\n")
    results.write("\n")

    open_stack, closed_stack, computational_time = AstarAlgorithm.Astar_Algorithm(initial_state, perf_counter(), True)
    search_path = UtilClass.get_search_path(initial_state, closed_stack)
    solution_path = UtilClass.get_solution_path(initial_state, closed_stack)
    
    results.write("A STAR HEURISTIC 1: MANHATTAN DISTANCE => " + str(computational_time) + "secs \n")
    
    results.write("Solution path: \n")
    results.write(str(solution_path) + "\n")
    results.write("\n")

    results.write("Search path: \n")
    results.write(str(search_path) + "\n")
    results.write("\n")
    
    open_stack, closed_stack, computational_time = AstarAlgorithm.Astar_Algorithm(initial_state, perf_counter(), False)
    search_path = UtilClass.get_search_path(initial_state, closed_stack)
    solution_path = UtilClass.get_solution_path(initial_state, closed_stack)
    
    results.write("A STAR HEURISTIC 2: SUM OF PERMUTATIONS => " + str(computational_time) + "secs \n")
    
    results.write("Solution path: \n")
    results.write(str(solution_path) + "\n")
    results.write("\n")

    results.write("Search path: \n")
    results.write(str(search_path) + "\n")
    results.write("\n")
    
    results.write("*********************************************************************************\n\n")

results.close()
inputs.close()