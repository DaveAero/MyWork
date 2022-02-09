# lab4.1.3-gradeRounding.py
# This program is used to convert percentage to a grade with arounding of percentages
# author: David Burke

# prompt user to input a percentage
percent = float(input("Enter the percentage:"))

# check if the percentage is valit 0 <= X <= 100
if (percent < 0) or (percent > 100):
    print("Please enter a valid number")

## Rounding of percentages ##
percentRound = int(round(percent))

# check with grade the number falls into
# if the range matches then print the below string
# if not move to next elif range check
if (percentRound < 40):
    print("Fail")

elif ((percentRound >= 40) and (percentRound < 50)):
    print("Pass")

elif ((percentRound >= 50) and (percentRound < 60)):
    print("Merit 2")

elif ((percentRound >= 60) and (percentRound < 70)):
    print("Merit 1")

elif (percentRound >= 70):
    print("Distinction")