# lab3.1.5-randomfruit.py
# This program is used to select a random fruit
# author: David Burke

# import modules
import random

# intro
print("Random fruit generator.")

# defining fruit list
fruits = ['Apple', 'Orange', 'Banana', 'Pear']

# generating the random index number between 0 and lenght-1
# length-1 is used as a list index starts at 0 not 1
index = random.randint(0,len(fruits)-1)

# converting index number to fruit
selected_fruit = fruits[index]

# printing the winning fruit
print("A Random Fruit: {}".format(selected_fruit))