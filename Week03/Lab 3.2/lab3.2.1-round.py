# lab3.2.1-round.py
# This program is used to round floating numbers to intigers
# author: David Burke

# Prompt the user to input a number
float_number = float(input("Enter a floating number:"))

# Round the number to the nearest intiger
int_number = round(float_number)

# print output
print("{} rounded is {}".format(float_number, int_number))