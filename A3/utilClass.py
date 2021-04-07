# Team Members:
# Zach Eichler 40018021
# Irina Patrocinio-Frazao 40024714
# Emilie Mines 40045370

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