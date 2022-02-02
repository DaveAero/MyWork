# lab3.2.4-convert.py
# This program is used to convert floating numbers of Euro, to positive whole numbers of Cents
# author: David Burke

# Prompt the user to input a number
float_num_euro = float(input("Please enter an amount:"))

# Convert negative numbers to positive
float_num_euro_pos = abs(float_num_euro)

# multiply numbers 10^2 to move the decial point 2 postions to the right
# redefine the number as cents reather than euros
int_num_cent = int(float_num_euro_pos * 10**2)

# print results
print("That amount in cent is: {}".format(int_num_cent))