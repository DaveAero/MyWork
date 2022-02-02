# lab3.1.3-div.py
# This program is used as a division calculator
# author: David Burke

# intro
print("Division Calculator")
print("Whole numbers only please!!")

# prompt users to input numbers
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter the number you want to divide by: "))

# calculate the division
answer = int(num_1//num_2)
remainder = num_1 % num_2

# print final answer
print("{} divided by {} is {} with remainder {}.".format(num_1, num_2, answer, remainder))