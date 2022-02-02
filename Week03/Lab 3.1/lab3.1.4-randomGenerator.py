# lab3.1.4-randomGenerator.py
# This program is used to generate a random number between 1 and 10
# author: David Burke

# import modules
import random

# intro
print("Random number generator")

#select range
range = int(input("Choose the range for the random number generator: "))

# generate random number
num_1 = random.randint(1,range)

# print result
print("Here is a random number {}".format(num_1))