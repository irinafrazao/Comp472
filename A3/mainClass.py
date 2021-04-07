# Team Members:
# Zach Eichler 40018021
# Irina Patrocinio-Frazao 40024714
# Emilie Mines 40045370

import utilClass

print("\nWelcome to the PNT game!")
print("Let's start!")

while True:
    print("\nGive me a sequence of positive integers separated by spaces in this format:")
    print("<#tokens><#taken_tokens><list_of_taken_tokens><depth>")

    inputString = input()
    
    total_tokens, number_of_taken_tokens, list_of_taken_tokens, depth = utilClass.split_input_string(inputString)
    
    print("This is what you gave me: " + str(total_tokens) + "  " + str(number_of_taken_tokens) + "   " + str(list_of_taken_tokens) + "   " + str(depth))
