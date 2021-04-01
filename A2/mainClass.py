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

# # each line of file is one puzzle
inputs = open("inputs.txt", "r")


for index, initial_state in enumerate(inputs):

     #turn string from input into a python obj (tuple of tuple)
     initial_state = eval(initial_state)    
 
 
     results.write("Puzzle " + str(index + 1) + ": " + str(initial_state) + "\n")
     
     open_stack, closed_stack, computational_time = DepthFirstSearch.depth_first_search(initial_state, False, 0, perf_counter()) 
     search_path = UtilClass.get_search_path(initial_state, closed_stack)
     solution_path,solution_cost = UtilClass.get_solution_path(initial_state, closed_stack,False)
     
     results.write("DEPTH FIRST SEARCH => " + str(computational_time) + "secs \n")
     
     results.write("Solution path: \n")
     results.write(str(solution_path) + "\n")
     results.write("\n")
 
     results.write("Search path: \n")
     results.write(str(search_path) + "\n")
     results.write("\n")
     results.write("Solution Cost: " + str(solution_cost) + "\n")
     results.write("\n")
     
     
 
     open_stack, closed_stack, computational_time = IterativeDeepeningSearch.iterative_deepening_search(initial_state) 
     search_path = UtilClass.get_search_path(initial_state, closed_stack)
     solution_path,solution_cost = UtilClass.get_solution_path(initial_state, closed_stack,False)
 
     results.write("ITERATIVE DEEPENING => " + str(computational_time) + "secs \n")
     
     results.write("Solution path: \n")
     results.write(str(solution_path) + "\n")
     results.write("\n")
 
     results.write("Search path: \n")
     results.write(str(search_path) + "\n")
     results.write("\n")
     results.write("Solution Cost: " + str(solution_cost) + "\n")
     results.write("\n")
 
     open_stack, closed_stack, computational_time = AstarAlgorithm.Astar_Algorithm(initial_state, perf_counter(), True,False)
     search_path = UtilClass.get_search_path(initial_state, closed_stack)
     solution_path,solution_cost = UtilClass.get_solution_path(initial_state, closed_stack,True)
     
     results.write("A STAR HEURISTIC 1: MANHATTAN DISTANCE => " + str(computational_time) + "secs \n")
     
     results.write("Solution path: \n")
     results.write(str(solution_path) + "\n")
     results.write("\n")
 
     results.write("Search path: \n")
     results.write(str(search_path) + "\n")
     results.write("\n")
     results.write("Solution Cost: " + str(solution_cost) + "\n")
     results.write("\n")
     
     open_stack, closed_stack, computational_time = AstarAlgorithm.Astar_Algorithm(initial_state, perf_counter(), False,False)
     search_path = UtilClass.get_search_path(initial_state, closed_stack)
     solution_path,solution_cost = UtilClass.get_solution_path(initial_state, closed_stack,True)
     
     results.write("A STAR HEURISTIC 2: SUM OF PERMUTATIONS => " + str(computational_time) + "secs \n")
     
     results.write("Solution path: \n")
     results.write(str(solution_path) + "\n")
     results.write("\n")
 
     results.write("Search path: \n")
     results.write(str(search_path) + "\n")
     results.write("\n")
     results.write("Solution Cost: " + str(solution_cost) + "\n")
     results.write("\n")
     
     
     results.write("*********************************************************************************\n\n")
 
results.close()
inputs.close()




# for 4x4 scaled puzzle (UNCOMMENT WHEN WE NEED TO RUN - CTRL 4 and CTRL 1 SHORTCUTS)

# =============================================================================
# 
# scaled_results_4 = open("scaled_results_4.txt","w")
# scaled_inputs_4 = open("scaled_inputs_4.txt","r")
# 
# for index, initial_state in enumerate(scaled_inputs_4):
#     initial_state = eval(initial_state)
#     scaled_results_4.write("Puzzle " + str(index + 1) + ": " + str(initial_state) + "\n")
#     
#     open_stack, closed_stack, computational_time = AstarAlgorithm.Astar_Algorithm(initial_state, perf_counter(),True,True)
#     search_path = UtilClass.get_search_path(initial_state, closed_stack)
#     solution_path,solution_cost = UtilClass.get_solution_path(initial_state, closed_stack,True)
#     
#     scaled_results_4.write("A STAR HEURISTIC 1: MANHATTAN DISTANCE => " + str(computational_time) + "secs \n")
#      
#     scaled_results_4.write("Solution path: \n")
#     scaled_results_4.write(str(solution_path) + "\n")
#     scaled_results_4.write("\n")
#  
#     scaled_results_4.write("Search path: \n")
#     scaled_results_4.write(str(search_path) + "\n")
#     scaled_results_4.write("\n")
#     scaled_results_4.write("Solution Cost: " + str(solution_cost) + "\n")
#     scaled_results_4.write("\n")
#      
#     scaled_results_4.write("*********************************************************************************\n\n")
#  
# scaled_inputs_4.close()
# scaled_results_4.close()
# 
# =============================================================================



# for 5x5 scaled puzzle (UNCOMMENT WHEN WE NEED TO RUN - CTRL 4 and CTRL 1 SHORTCUTS)

# =============================================================================

# scaled_results_5 = open("scaled_results_5.txt","w")
# scaled_inputs_5 = open("scaled_inputs_5.txt","r")
  
# for index, initial_state in enumerate(scaled_inputs_5):
      
#       scaled_results_5.write("puzzle " + str(index + 1) + ": " + str(initial_state) + "\n")
#       initial_state = eval(initial_state)
#       open_stack, closed_stack, computational_time = astaralgorithm.astar_algorithm(initial_state, perf_counter(), true,true)
#       search_path = utilclass.get_search_path(initial_state, closed_stack)
#       solution_path,solution_cost= utilclass.get_solution_path(initial_state, closed_stack,true)
      
#       scaled_results_5.write("a star heuristic 1: manhattan distance => " + str(computational_time) + "secs \n")
      
#       scaled_results_5.write("solution path: \n")
#       scaled_results_5.write(str(solution_path) + "\n")
#       scaled_results_5.write("\n")
  
#       scaled_results_5.write("search path: \n")
#       scaled_results_5.write(str(search_path) + "\n")
#       scaled_results_5.write("\n")
#       scaled_results_5.write("solution cost: " + str(solution_cost) + "\n")
#       scaled_results_5.write("\n")
#       scaled_results_5.write("*********************************************************************************\n\n")
  
# scaled_inputs_5.close()
# scaled_results_5.close()


# =============================================================================
