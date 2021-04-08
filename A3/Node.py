# Team Members:
# Zach Eichler 40018021
# Irina Patrocinio-Frazao 40024714
# Emilie Mines 40045370

class Node:
    
    # parent: the whole parent node
    # maximizingPLayer: boolean to say if the node is on a MAX layer
    # total_tokens: (int) number of tokens the game started with
    # list_taken_tokens: the list of taken tokens
    # depth_of_node: depth in the tree where this node resides
    # list_children: list of children nodes
    # move_PNT: the move this node represents (which number is taken out)
    def __init__(self, parent, maximizingPlayer, total_tokens, list_taken_tokens, depth_of_node, list_children, move_PNT):
        self.parent = parent
        self.maximizingPlayer = maximizingPlayer
        self.total_tokens = total_tokens
        self.list_taken_tokens = list_taken_tokens
        self.depth_of_node = depth_of_node
        self.list_children = list_children
        self.move_PNT = move_PNT
        
    def print_node(self):
        print("parent: ", self.parent)
        print("maximizingPlayer: ", self.maximizingPlayer)
        print("total_tokens: ", self.total_tokens)
        print("list_taken_tokens: ", self.list_taken_tokens)
        print("depth_of_node: ", self.depth_of_node)
        print("list_children: ", self.list_children)
        print("move_PNT: ", self.move_PNT)
        print("\n")

