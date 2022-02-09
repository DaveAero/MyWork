# lab4.1.1-isEven.py
# This program is used to test if a number is even or odd
# author: David Burke

# prompt user to enter a number
number = int(input("Enter a number:"))

# use an if statement to first test if the number is even / divisable by 2
# if not even then the number must be odd
if (number % 2) == 0:
    print ("{} is an even number".format(number))

else:
    print("{} is an odd number".format(number))