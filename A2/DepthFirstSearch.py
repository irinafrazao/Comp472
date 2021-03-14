# Team Members:
# Zach Eichler 40018021
# Irina Patrocinio-Frazao 40024714
# Emilie Mines 40045370

from Node import Node
from Node import Directions
from random import randrange

def depth_first_search(initial_puzzle_board):
    #append() = add elements to the top of stack, pop() = removes the element in LIFO order. 
    open_stack = []
    closed_stack = []
    
    root_node = create_initial_node(initial_puzzle_board)
    open_stack.append(root_node)
    
    goal_state = get_goal_state_for_puzzle(initial_puzzle_board)

    counter = 0
    while len(open_stack) != 0:
        currentNode = open_stack.pop()

        if currentNode.state != goal_state:
            print("not goal state yet")
            closed_stack.append(currentNode)
            
            children = get_all_children_of_node(currentNode)
            filtered_children = get_children_to_add_to_open_stack(open_stack, closed_stack, children)

            for child in filtered_children:
                open_stack.append(child)
                
            print("loop " + str(counter))
            print(len(open_stack))

            
            counter = counter + 1
            
        elif currentNode.state == goal_state:
            print("success")
            return open_stack, closed_stack
    
    # if it gets out of the loop, exit with failure
    
def create_initial_node(initial_puzzle_board):
    
    # initial node doesnt have a parent or direction, state didnt move yet
    parent_state = None
    direction = None
    
    # Arbitrary take FIRST puzzle piece, this piece will move the whole time
    index_to_move = (0,0)

    state = initial_puzzle_board
    depth = 0

    root_node = Node(parent_state,direction,index_to_move,state,depth)
    return root_node

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
    

def get_children_to_add_to_open_stack(open_stack, closed_stack, children):
    children_to_add = []
    
    add_to_open_stack = True
    add_to_closed_stack = True
    
    for child in children:
        if open_stack != []:
            for open_node in open_stack:
                if open_node.state is not None:
                    if Node.compare_equality_2_nodes(open_node, child):
                        add_to_open_stack = False
               
        if closed_stack != []:
            for closed_node in closed_stack:
                if closed_node.state is not None:
                    if Node.compare_equality_2_nodes(closed_node, child):
                        add_to_closed_stack = False
                        
        if add_to_closed_stack == True and add_to_open_stack == True:
            children_to_add.append(child)
            
    return children_to_add
           
    
def get_new_index_after_move(index_to_move, direction):
    if direction is Directions.Up:
        new_row_index = index_to_move[1] - 1
        new_col_index = index_to_move[0]
        
    if direction is Directions.Down:
        new_row_index = index_to_move[1] + 1
        new_col_index = index_to_move[0]
        
    if direction is Directions.Left:
        new_row_index = index_to_move[1]
        new_col_index = index_to_move[0] - 1
        
    if direction is Directions.Right:
        new_row_index = index_to_move[1]
        new_col_index = index_to_move[0] + 1
        
    return (new_col_index, new_row_index)
       

def can_puzzle_move(index_to_move, size):
    if index_to_move[0] < 0 or index_to_move[1] < 0:
        return False
    
    if index_to_move[0] >= size or index_to_move[1] >= size:
        return False
    
    return True


def get_state_after_move(parent_state, index_to_move, direction):
    
    new_index = get_new_index_after_move(index_to_move, direction)
    
    # get all values in puzzle
    values = [] 
    for t in parent_state:
        for value in t:
            values.append(value)
            
    size_board = len(parent_state)

    # switch 2 positions in puzzle
    position1 = index_to_move[0] + (index_to_move[1]  * size_board)
    position2 = new_index[0] + (new_index[1] * size_board)
    
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


def get_all_children_of_node(currentNode):
    
    children = []
    
    counter = 0
    directionCtrs = []
    while counter < len(Directions):
    
        # bit of randomness in direction
        directionCtr = randrange(4)
        while directionCtr is directionCtrs:
            directionCtr = randrange(4)
        directionCtrs.append(directionCtr);
        
        # checking if this direction works
        index_to_move = get_new_index_after_move(currentNode.index_move, Directions(directionCtr))
        can_it_move = can_puzzle_move(index_to_move, len(currentNode.state))

        if can_it_move == False:
            counter = counter + 1
            continue;
        else:
            # build node
            parent = currentNode
            depth = currentNode.depth + 1
            direction = Directions(directionCtr)
        
            state = get_state_after_move(currentNode.state, currentNode.index_move, Directions(directionCtr))                                                       
                                  
            node = Node(parent, direction, index_to_move, state, depth)
            children.append(node)  
        
            counter = counter + 1

    return children;                                            
        