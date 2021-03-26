#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 22:29:48 2021

@author: zacheichler
"""

import UtilClass
    

def sum_of_permutations (initial_puzzle_board):
    
    print("starting sum of permutations")
        
    open_stack = []
    closed_stack = []
    goal_state = UtilClass.get_goal_state_for_puzzle(initial_puzzle_board)
    found_goal = False
        
    #flattened 2D state to calculate sum of permutations
    initial_state_2D = UtilClass.flatten(initial_puzzle_board)
    
    #calculate initial h with sum of permutations
    initial_h = UtilClass.get_sum_of_permutations(initial_state_2D)
        
      
    #creates heuristic node with depth, f value (depth+calculated h)
    root_node = UtilClass.create_initial_heuristic_Node(initial_puzzle_board, initial_h)
        
    #get all the possible swaps
    possible_swaps = UtilClass.get_possible_position_swaps(root_node);
  
       
    #add initial node to stack
    open_stack.append(root_node)
        
    #loop until either open stack is empty or solution is found    
    while True:
        #check if open stack is empty
        if len(open_stack) == 0:
            print("No solution found :(")
            break;
        #get current node from stack
        current_node = open_stack.pop()
        #add current node to closed stack
        closed_stack.append(current_node)
        #check if current node is goal state
        if current_node.state == goal_state:
            print("woo")
            break;
        #Generate all possible children with g,h,f values using sum of permutations
        children = UtilClass.get_all_children_of_sum_of_permutation_node(current_node, possible_swaps)
        #filter to find those not in closed or open
        children_to_add = UtilClass.filter_children_heuristic(open_stack, closed_stack, children)
        #add filtered children to open stack
        for i in children_to_add:
            open_stack.append(i)
        
        #sort open stack by fval
        open_stack.sort(key=lambda x: x.fval)
        #reverse open stack so lowest fval is at the top
        open_stack.reverse()
        
        
            
        
                

                
                   
                  
               
                
        
        
        
        
                       
                       
     
                       
                       
                       
                       #if new_F_Node.get("node").state == closed_stack[j].get("node").state:
                       #    print("already added")
                       #else:
                        #   open_stack.append(new_F_Node)
                         #  print("added: ",new_F_Node.get("node").state, "" , new_F_Node.get("f"))
                          
                   
                   
        
            
    
        
        
        
        
        
        
       
        
      
        #print(goal_state_2D)
        #print(initial_state_2D)
        #print(UtilClass.get_distance(initial_state_2D))
        
        #loop through array starting at each value,
        # get position of value
        # check all following values and count how many should be before
        
     