# Team Members:
# Zach Eichler 40018021
# Irina Patrocinio-Frazao 40024714
# Emilie Mines 40045370

import utilClass
import math

print("\nWelcome to the PNT game!")
print("Let's start and compute a single move!")

while True:
    print("\nGive me a sequence of positive integers separated by spaces in this format:")
    print("<#tokens><#taken_tokens><list_of_taken_tokens><depth>")

    # collect input
    inputString = input()
    
    total_tokens, number_of_taken_tokens, list_of_taken_tokens, depth_of_search_tree = utilClass.split_input_string(inputString)

    # create root of tree
    treeRootNode = utilClass.create_root_node(total_tokens, list_of_taken_tokens, number_of_taken_tokens, depth_of_search_tree)
    
    # send data to alpha beta algorithm
    count_nodes_visited = 1
    count_nodes_evaluated = 0
    max_depth_reached = 0
    branching_factor_total_children = 0
    
    value, move_to_do, count_nodes_visited, count_nodes_evaluated, max_depth_reached, branching_factor_total_children = utilClass.alphabeta(treeRootNode, depth_of_search_tree, -math.inf, math.inf, True, count_nodes_visited, count_nodes_evaluated, max_depth_reached, branching_factor_total_children)
    
    print(branching_factor_total_children)
    branching_factor = count_nodes_visited / branching_factor_total_children
    
    print("VALUE TESTING: " + str(value) + "    MOVE:   " + str(move_to_do) + "   COUNT VISITED: " + str(count_nodes_visited))
    print("  COUNT EVALUATED: " + str(count_nodes_evaluated) + "   MAX DEPTH REACHED: " + str(max_depth_reached) + "   BRANCHING FACTOR: " + str(branching_factor))
    # TO ADD OUTPUT
    