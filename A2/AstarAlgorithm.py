# Team Members:
# Zach Eichler 40018021
# Irina Patrocinio-Frazao 40024714
# Emilie Mines 40045370

import UtilClass
from time import perf_counter

def Astar_Algorithm(initial_puzzle_board, startTime, manhattan):
    
    if manhattan == True: 
        print("starting manhattan distance")
    else:
         print("starting sum of permutations")
    
    timerThresholdInSeconds = 60
    timesUp = False
    
    open_stack = []
    closed_stack = []
    goal_state = UtilClass.get_goal_state_for_puzzle(initial_puzzle_board)

    if manhattan == True:
        #calculate initial h with manhattan distance
        initial_h = UtilClass.get_manhattan_distance(goal_state,initial_puzzle_board)
    else:
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
    
    while True:
        
        # 60 secs timer for calculation
        endTime = perf_counter()
        if endTime - startTime >= timerThresholdInSeconds:
            timesUp = True
            break;
        
        if len(open_stack) == 0:
            print("No solution found :(")
            break;
            
        current_node = open_stack.pop()
        closed_stack.append(current_node)
        
        if current_node.state == goal_state:
            print("SUCCESS")
            break;
        
        if manhattan == True:
            print("searching manhattan.. " + str(endTime - startTime) + "secs")
            children = UtilClass.get_all_children_of_manhattan_distance_node(current_node, possible_swaps, goal_state)
        else:
            print("searching sum of permutations.. " + str(endTime - startTime) + "secs")
            #Generate all possible children with g,h,f values using sum of permutations
            children = UtilClass.get_all_children_of_sum_of_permutation_node(current_node, possible_swaps)
    
        #filter to find those not in closed or open
        children_to_remove_from_open_list, children_to_remove_from_closed_list, children_to_add = UtilClass.filter_children_heuristic(open_stack, closed_stack, children)


        for o in children_to_remove_from_open_list:
            open_stack.remove(o)
            
        for c in children_to_remove_from_closed_list:
            closed_stack.remove(c)

        for i in children_to_add:
            open_stack.append(i)
        
            
        #sort children by f value:
        open_stack.sort(key=lambda x: x.fval)
        
        #reverse open stack
        open_stack.reverse()
    
    # return outcome here
    computational_time = perf_counter() - startTime
    if timesUp == True:
        return None, None, computational_time
    else: 
        return open_stack, closed_stack,computational_time