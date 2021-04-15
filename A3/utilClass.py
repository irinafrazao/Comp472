# Team Members:
# Zach Eichler 40018021
# Irina Patrocinio-Frazao 40024714
# Emilie Mines 40045370

from Node import Node
import math

# read input string into the different values
def split_input_string(inputStr):
    array_of_values = inputStr.split();
    
    total_tokens = int(array_of_values.pop(0))
    number_of_taken_tokens = int(array_of_values.pop(0))
    
    list_of_taken_tokens = []
    if number_of_taken_tokens != 0:
        index = 0
        while index < number_of_taken_tokens:
            list_of_taken_tokens.append(int(array_of_values.pop(0)))
            index = index + 1
    
    depth = int(array_of_values.pop(0))
    
    return total_tokens, number_of_taken_tokens, list_of_taken_tokens, depth



def get_possible_moves_PNT(total_tokens, number_of_taken_tokens, list_of_taken_tokens):
    # first move, odd number strictly less than n/2
    if number_of_taken_tokens == 0:
        range_of_numbers = list(range(1, (int)(total_tokens/2 + 1)))
        possible_choices = [num for num in range_of_numbers if num % 2 == 1]
    # every subsequent move
    else:
        last_move = list_of_taken_tokens[-1]
        possible_choices = []
        for num in list(range(1, total_tokens + 1)):
            if num not in list_of_taken_tokens and is_multiple(num, last_move):
                possible_choices.append(num)
                
    return possible_choices


def assign_children_to_node(parentNode, number_of_taken_tokens, total_tokens, list_of_taken_tokens, depth_of_search_tree):

    # create nodes and add children to them  
    possible_moves = get_possible_moves_PNT(total_tokens, number_of_taken_tokens, list_of_taken_tokens)
    
    if parentNode.depth_of_node < depth_of_search_tree and len(possible_moves) > 0:
        depth_of_node = parentNode.depth_of_node + 1
        maximizingPlayerParent = not parentNode.maximizingPlayer

        for move in possible_moves:
            
            new_list_of_taken_moves = []
            for m in list_of_taken_tokens:
                new_list_of_taken_moves.append(m)
                
            new_list_of_taken_moves.append(move)
            
            childNode = Node(parentNode, maximizingPlayerParent, total_tokens, new_list_of_taken_moves, depth_of_node, [], move)    
            parentNode.list_children.append(childNode)
        
    return parentNode

    
def create_root_node(total_tokens, list_of_taken_tokens, number_of_taken_tokens, depth_of_search_tree):
    # root of tree has no parent and no move
    depth_of_node = 0   
    
    if number_of_taken_tokens == 0 or number_of_taken_tokens % 2 == 0:
        maximizingPlayerParent = True
    else:
        maximizingPlayerParent = False
        
    treeRoot = Node(None, maximizingPlayerParent, total_tokens, list_of_taken_tokens, depth_of_node, [], None)      
    
    treeRoot_with_children = assign_children_to_node(treeRoot, len(treeRoot.list_taken_tokens), treeRoot.total_tokens, treeRoot.list_taken_tokens, depth_of_search_tree)
    
    return treeRoot_with_children;
   

# logic of the alpha beta algorithm, compute a single move
def alphabeta(node, depth, alpha, beta, maximizingPlayer):
    
    # setup children of nodes (when its not the root node because it already comes with children)
    if node.parent is not None:
        node_with_children = assign_children_to_node(node, len(node.list_taken_tokens), node.total_tokens, node.list_taken_tokens, depth)
    else:
        node_with_children = node
        
    node_with_children.print_node()
    
    # we are at the max depth of tree or a terminal node, we need the e(n) value
    if depth == 0 or len(node_with_children.list_children) == 0:
        return static_board_evaluation(node_with_children)
    
    if maximizingPlayer:
        value = -math.inf
        for child in node_with_children.list_children:
            value = max(value, alphabeta(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if beta <= alpha:
                break # beta cut off branch
            return value
    else:
        value = math.inf
        for child in node_with_children.list_children:
            value = min(value, alphabeta(child, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                break # alpha cut off branch
            return value
    

# heuristic evaluation of a node
def static_board_evaluation(node):
    
    # end game state, the player on that layer loses, min wins = -1.0, max wins = 1.0
    if len(node.list_children) == 0:
        if node.maximizingPlayer:
            return -1.0
        else:
            return 1.0
         
    last_move = node.list_taken_tokens[-1]
    
    # if its MINs turn, the values are negated
    multiplier = 1
    if node.maximizingPlayer == False:
        multiplier = -1
    
    # token 1 not taken yet
    if 1 not in node.list_taken_tokens:
        return 0
    
    # token 1 was last move, count successors legal moves, odd = 0.5, even = -0.5
    if last_move == 1:
        if len(node.list_children) % 2 == 0:
            return multiplier * -0.5
        else:
            return multiplier * 0.5
    
    # last move was prime, count multiple of prime in successors, odd = 0.7, even = -0.7
    if is_prime(last_move):
        count = 0

        for child in node.list_children:
            if is_multiple(child.move_PNT, last_move):
                count = count + 1
        
        if count % 2 == 0:
            return multiplier * -0.7
        else:
            return multiplier * 0.7
        
    # last move is composite, find largest prime that can divide composite,
    # count multiples of that prime in successors, odd = 0.6, even = -0.6  
    if is_prime(last_move) == False:
        
        search = node.total_tokens
        while search > 0:
            if is_prime(search):
                if last_move % search == 0:
                    break
                else:
                    search = search - 1;
            else:
                search = search - 1;
                
        count = 0
        for child in node.list_children:
            if is_multiple(child.move_PNT, search):
                count = count + 1
        
        if count % 2 == 0:
            return multiplier * -0.6
        else:
            return multiplier * 0.6
        
        

# check if number_to_check is a multiple of number_multiple_of (4 is multiple of 2, i.e. 4 % 2 = 0)
def is_multiple(number_to_check, number_multiple_of):
    if number_to_check % number_multiple_of == 0:
        return True
    else:
        return False


# check if given number is prime or not  
def is_prime(number):

    # If given number is greater than 1
    if number > 1:
 
        # Iterate from 2 to number / 2
        for i in range(2, int(number/2)+1):
 
            # If number is divisible by any number between
            # 2 and nymber / 2, it is not prime
            if (number % i) == 0:
                return False
                break
            else:
                return True
    else:
        return False