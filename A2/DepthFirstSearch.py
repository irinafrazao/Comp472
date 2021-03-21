# Team Members:
# Zach Eichler 40018021
# Irina Patrocinio-Frazao 40024714
# Emilie Mines 40045370

import UtilClass

# apply depth first search algorithm on a puzzle to find the solution path
def depth_first_search(initial_puzzle_board, iterative_deepening, depth):
    
    #append() = add elements to the top of stack, pop() = removes the element in LIFO order. 
    open_stack = []
    closed_stack = []
    
    root_node = UtilClass.create_initial_node(initial_puzzle_board)
    open_stack.append(root_node)
    
    goal_state = UtilClass.get_goal_state_for_puzzle(initial_puzzle_board)
    possible_swaps = UtilClass.get_possible_position_swaps(root_node);

    nodes_visited_counter = 0
    
    while len(open_stack) != 0:
        currentNode = open_stack.pop()

        if currentNode.state != goal_state:
            print("searching..")
            closed_stack.append(currentNode)
            print("depth: " + str(currentNode.depth))
            
            children = UtilClass.get_all_children_of_node(currentNode, possible_swaps)
            unique_children_nodes = list(set(children))
            
            filtered_children = UtilClass.filter_children_to_add_to_open_stack(open_stack, closed_stack, unique_children_nodes, iterative_deepening, depth)

            for child in filtered_children:
                open_stack.append(child)
                
            print("nodes visited/ in closed list: " + str(nodes_visited_counter))
            print("number of nodes in open stack: " + str(len(open_stack)) + "\n")

            nodes_visited_counter = nodes_visited_counter + 1
            
        elif currentNode.state == goal_state:
            print("SUCCESS")
            closed_stack.append(currentNode)
            break;
    
    # if it returns here, FAILURE
    return open_stack, closed_stack
 