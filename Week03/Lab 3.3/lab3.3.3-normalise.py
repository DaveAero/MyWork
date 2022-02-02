# lab3.3.3-normalise.py
# This program reads in a string, removes leading or trailing spaces, coverts all text to lowercase and outputs the resulting string
# the lenth of the inital and resulting strings are output
# author: David Burke

# prompt the user to input a sting
raw_input = input("iN PUt stRiNG hERE:")

# remove all capital letters
lower_case_raw_input = raw_input.lower()

# remove all leading and trailing spaces
lower_case_normalised = lower_case_raw_input.strip()

# calculate lenth of input and output strings
input_len = len(raw_input)
output_len = len(lower_case_normalised)

# output results
print("The string normalised is: {}".format(lower_case_normalised))
print("The input string was reduced from {} to {} characters".format(input_len,output_len))