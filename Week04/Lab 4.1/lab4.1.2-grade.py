# lab4.1.2-grade.py
# This program is used to convert percentage to a grade
# author: David Burke

# prompt user to input a percentage
percent = float(input("Enter the percentage:"))

# check if the percentage is valit 0 <= X <= 100
if (percent < 0) or (percent > 100):
    print("Please enter a valid number")

# check with grade the number falls into
# if the range matches then print the below string
# if not move to next elif range check
elif (percent < 40):
    print("Fail")

elif ((percent >= 40) and (percent < 50)):
    print("Pass")

elif ((percent >= 50) and (percent < 60)):
    print("Merit 2")

elif ((percent >= 60) and (percent < 70)):
    print("Merit 1")

elif (percent >= 70):
    print("Distinction")