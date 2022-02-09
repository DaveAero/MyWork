# lab4.2.5-average.py
# This program is used to find the average of the entered numbers
# author: David Burke

# create the empty number list
numbers = []

number = int(input("Enter number (0 to quit): "))

while number != 0:
    numbers.append(number)

    # read the next number and check if 0
    number = int(input("Enter another (0 to quit): "))

for value in numbers:
    print (value)

average = float(sum(numbers)) / len(numbers)
print("The average is {}".format(average))