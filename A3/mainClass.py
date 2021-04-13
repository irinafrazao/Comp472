# Team Members:
# Zach Eichler 40018021
# Irina Patrocinio-Frazao 40024714
# Emilie Mines 40045370

import utilClass
import Node
import math

print("\nWelcome to the PNT game!")
print("Let's start!")

while True:
    print("\nGive me a sequence of positive integers separated by spaces in this format:")
    print("<#tokens><#taken_tokens><list_of_taken_tokens><depth>")

    # collect input
    inputString = input()
    
    total_tokens, number_of_taken_tokens, list_of_taken_tokens, depth_of_search_tree = utilClass.split_input_string(inputString)
    
    print("DEBUG: This is what you gave me: " + str(total_tokens) + "  " + str(number_of_taken_tokens) + "   " + str(list_of_taken_tokens) + "   " + str(depth_of_search_tree))
    
    # create tree
    tree = utilClass.build_search_tree(total_tokens, list_of_taken_tokens, number_of_taken_tokens, depth_of_search_tree)
    
    # send data to alpha beta algorithm
    value = utilClass.alphabeta(tree, depth_of_search_tree, -math.inf, math.inf, True)
    print("VALUE TESTING: " + str(value))
    
    # Test tree some more to make sure its well built!!
    
    # TO ADD OUTPUT
    