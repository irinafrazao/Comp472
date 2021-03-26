#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 22:24:29 2021

@author: zacheichler
"""

import UtilClass

def manhattan_distance(initial_puzzle_board):
    print("starting manhattan distance")
    
    

    open_stack = []
    closed_stack = []
    goal_state = UtilClass.get_goal_state_for_puzzle(initial_puzzle_board)
    found_goal = False
    initial_h = UtilClass.get_manhattan_distance(goal_state,initial_puzzle_board)
    
    #calculate initial h with manhattan distance
    initial_h = UtilClass.get_manhattan_distance(goal_state,initial_puzzle_board)
    
    #creates heuristic node with depth, f value (depth+calculated h)
    root_node = UtilClass.create_initial_heuristic_Node(initial_puzzle_board, initial_h)
    
    
    #get all the possible swaps
    possible_swaps = UtilClass.get_possible_position_swaps(root_node);
    
    #add initial node to stack
    open_stack.append(root_node)
    
    
    while True:
        if len(open_stack) == 0:
            print("No solution found :(")
            break;
        current_node = open_stack.pop()
        closed_stack.append(current_node)
        if current_node.state == goal_state:
            print("wooo")
            break;
        children = UtilClass.get_all_children_of_manhattan_distance_node(current_node, possible_swaps, goal_state)
        children_to_add = UtilClass.filter_children_heuristic(open_stack, closed_stack, children)
    
        for i in children_to_add:
            open_stack.append(i)
        #sort children by f value:
        open_stack.sort(key=lambda x: x.fval)
        #reverse open stack
        open_stack.reverse()
        