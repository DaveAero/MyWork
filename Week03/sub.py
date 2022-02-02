# sub.py
# This program is used as a subraction calculator
# author: David Burke

# intro
print("Subtraction Calculator")
print("Whole numbers only please")

# prompt users to input numbers
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

# calculate the subraction
answer = num_1 - num_2

# print final answer
print("{} minus {} is {}.".format(num_1, num_2, answer))
