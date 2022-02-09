# lab4.1.4-while.py
# This program is used to spam a user until they enter -1
# author: David Burke

# prompt user to enter initial number to start the madness
number = int(input("Enter a number:"))

# prompt user to enter a number
while number != -1:
    number = int(input("Enter a better number:"))

print("Alas, the best number was -1 all along")