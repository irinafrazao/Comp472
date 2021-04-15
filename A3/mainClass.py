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
    value = utilClass.alphabeta(treeRootNode, depth_of_search_tree, -math.inf, math.inf, True)
    print("VALUE TESTING: " + str(value))
    
    # TO ADD OUTPUT
    