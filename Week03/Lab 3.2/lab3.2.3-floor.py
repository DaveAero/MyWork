# lab3.2.3-floor.py
# This program takes a number and returns the number rounded down
# author: David Burke

# import modules
import math

# Prompt the user to input a floating number
float_number = float(input("Enter at floating number:"))

# Round down the entered number
floor_number = math.floor(float_number)

# print result
print("{} floored is {}".format(float_number,floor_number))