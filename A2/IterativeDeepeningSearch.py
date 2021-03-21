# Team Members:
# Zach Eichler 40018021
# Irina Patrocinio-Frazao 40024714
# Emilie Mines 40045370

import UtilClass
import DepthFirstSearch 

# apply iterative deepening search algorithm on a puzzle to find the solution path
def iterative_deepening_search(initial_puzzle_board):
    
    depth = 0
    foundGoal = False
    
    goal_state = UtilClass.get_goal_state_for_puzzle(initial_puzzle_board)
    
    while foundGoal == False:
        open_stack, closed_stack = DepthFirstSearch.depth_first_search(initial_puzzle_board, True, depth)
        lastNodeVisited = closed_stack.pop()
        
        if lastNodeVisited.state != goal_state:
            depth = depth + 1
            foundGoal = False
        else:
            closed_stack.append(lastNodeVisited)
            foundGoal = True
            break;
    
    return open_stack, closed_stack