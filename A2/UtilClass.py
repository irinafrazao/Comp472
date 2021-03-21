# Team Members:
# Zach Eichler 40018021
# Irina Patrocinio-Frazao 40024714
# Emilie Mines 40045370

from Node import Node
   
# make the initial node using the input puzzle
def create_initial_node(initial_puzzle_board):
    
    # initial node doesnt have a parent
    parent_state = None
    
    # initial node didnt move anything yet
    indexes_move_1 = None
    indexes_move_2 = None

    state = initial_puzzle_board
    depth = 0

    root_node = Node(parent_state,indexes_move_1,indexes_move_2,state,depth)
    return root_node

# get the goal state to know when the puzzle is sloved
def get_goal_state_for_puzzle(initial_puzzle_board):
    
    # get all values in puzzle
    values = [] 
    for t in initial_puzzle_board:
        for value in t:
            values.append(value)
            
    # sort values (min to max)
    values.sort()
    
    # make new n-tuple of n-tuples in order
    size = len(initial_puzzle_board)
    
    start = 0
    end = size
    temp_list = []
    while end <= len(values):
        temp_list.append((values[start:end]))
        start = start + size
        end = end + size
        
    goal_state = tuple(tuple(x) for x in temp_list)

    return goal_state
    
	
# double check if children are already in the closed list to avoid cycles
def filter_children_to_add_to_open_stack(open_stack_nodes, closed_stack_nodes, children_nodes, iterative_deepening, depth):
    children_to_add = []
    
    closed_states = [c.state for c in closed_stack_nodes]
    open_states = [o.state for o in open_stack_nodes]

    if closed_stack_nodes != []:
        for child in children_nodes: 
            if iterative_deepening == True:
                if child.depth <= depth:
                    if child.state not in closed_states and child.state not in open_states:
                        children_to_add.append(child)
            else:
                if child.state not in closed_states and child.state not in open_states:
                    children_to_add.append(child)
                       
                                                  
    return children_to_add
	
           
# apply swap to a state
def get_state_after_move(parent_state, indexes_move_1, indexes_move_2):
    
    # get all values in puzzle
    values = [] 
    for t in parent_state:
        for value in t:
            values.append(value)
            
    size_board = len(parent_state)

    # switch 2 positions in puzzle
    position1 = (indexes_move_1[0] * size_board) + indexes_move_1[1]
    position2 = (indexes_move_2[0] * size_board) + indexes_move_2[1]
    
    values[position1], values[position2] = values[position2], values[position1] 
    
    # make new n-tuple of n-tuples 
    size = len(parent_state)
    
    start = 0
    end = size
    temp_list = []
    while end <= len(values):
        temp_list.append((values[start:end]))
        start = start + size
        end = end + size

    children_state = tuple(tuple(x) for x in temp_list)

    return children_state


# getting all possibile sideways and updown swipes (3x3 = 6 sideways and 6 updown)
def get_possible_position_swaps(currentNode):
    swaps = []
    
    size = len(currentNode.state)
    
    row_ctr = 0
    col_ctr= 0
    
    # getting swap that are side to side.
    while row_ctr != size:
        pos1 = (row_ctr, col_ctr)
        col_ctr = col_ctr + 1
        pos2 = (row_ctr, col_ctr )
        swap = (pos1, pos2)
        swaps.append(swap)
        if col_ctr == size - 1:
            col_ctr = 0;
            row_ctr = row_ctr + 1
            
    row_ctr = 0
    col_ctr = 0
            
    # getting swap that are up and down.
    while col_ctr != size:
        pos1 = (row_ctr, col_ctr)
        row_ctr = row_ctr + 1
        pos2 = (row_ctr, col_ctr )
        swap = (pos1, pos2)
        swaps.append(swap)
        if row_ctr == size - 1:
            row_ctr = 0;
            col_ctr = col_ctr + 1
            
    return swaps
        


# making all children nodes, one for each possible swap
def get_all_children_of_node(currentNode, possible_swaps):
    
    children = []
    new_depth = currentNode.depth + 1
    
    for swap in possible_swaps:
        parent = currentNode
        depth = new_depth
        indexes_move_1 = swap[0]
        indexes_move_2 = swap[1]
        state = get_state_after_move(currentNode.state, indexes_move_1, indexes_move_2)                        

        node = Node(parent, indexes_move_1, indexes_move_2, state, depth)    
        children.append(node)   

    return children                              


# get the solution path from the closed_list after search algorithm is over
# TODO: no solution by timer
# TODO: true no solution (ended in timer but last node visited is not goal)
def get_solution_path(initial_puzzle_state, closed_stack):
    
    solution_path = str(initial_puzzle_state) + "\n"
    reversedPathStates = [];
    
    goalNode = closed_stack.pop()
    currentNode = goalNode
    
    while currentNode.parent.state != initial_puzzle_state:
        for node in closed_stack:
            if node.state == currentNode.parent.state:
                reversedPathStates.append(node.state)
                currentNode = node
                break
    
    reversedPathStates.reverse()
    for path_state in reversedPathStates:
        solution_path = solution_path + str(path_state) + "\n"
        
    solution_path = solution_path + str(goalNode.state)
    
    return solution_path
    
    
# get the search path from the closed_list after search algorithm is over
# TODO: no solution by timer
# TODO: true no solution (ended in timer but last node visited is not goal)
def get_search_path(closed_stack):
    
    search_path = ""
    
    closed_states = [c.state for c in closed_stack]

    for state in closed_states:
        search_path = search_path + str(state) + "\n"

    return search_path
    
    
    
    
    
    
    
    