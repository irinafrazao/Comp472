# Team Members:
# Zach Eichler 40018021
# Irina Patrocinio-Frazao 40024714
# Emilie Mines 40045370

import utilClass
import math
from time import perf_counter

# read test case inputs from file
test_cases = []
inputs = open("testcases.txt", "r")

for inputString in inputs:
    tokens = inputString.partition("TakeTokens")[2]
    test_cases.append(tokens)

# for each input from file...
count = 1
for inputString in test_cases:
    
    inputString = inputString.rstrip()
    
    # collect input
    print("___________")
    print("Test Case: " + str(count))
    print(inputString)
    print("___________")
    count += 1
    
    total_tokens, number_of_taken_tokens, list_of_taken_tokens, depth_of_search_tree = utilClass.split_input_string(inputString)

    # create root of tree
    treeRootNode = utilClass.create_root_node(total_tokens, list_of_taken_tokens, number_of_taken_tokens, depth_of_search_tree)
    
    # send data to alpha beta algorithm
    count_nodes_visited = 1
    count_nodes_evaluated = 0
    max_depth_reached = 0
    branching_factor_total_children = 1
    
    start = perf_counter()
    value, move_to_do, count_nodes_visited, count_nodes_evaluated, max_depth_reached, branching_factor_total_children = utilClass.alphabeta(treeRootNode, depth_of_search_tree, -math.inf, math.inf, True, count_nodes_visited, count_nodes_evaluated, max_depth_reached, branching_factor_total_children)
    end = perf_counter()
    
    execution_time = end-start
    
    if branching_factor_total_children == 0:
        branching_factor = 0
    else:
        branching_factor = round((count_nodes_visited / branching_factor_total_children),1)
    
    # print output
    print("OUTPUT!")
    print("Move: " + str(move_to_do))
    print("Value: " + str(value))
    print("Number of Nodes Visited: " + str(count_nodes_visited))
    print("Number of Nodes Evaluated: " + str(count_nodes_evaluated))
    print("Max Depth Reached: " + str(max_depth_reached))
    print("Avg Effective Branching Factor: " + str(branching_factor))
    print("Execution Time: " + str(execution_time) + "secs" + "\n")