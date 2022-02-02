# lab3.1.1-TestTypes.py
# This program is used to test Variable Types
# author: David Burke

# Defining the variables of each type
whole_number = int(3)
floating_number = 3.5
boolean_true = True
test_text = "Bools and Ghouls"
list = [ 1 , 1.5 , "1" , False]

# printing each of the variables,
# first naming the variable using print()
# secondly typing the variable using type()
# finally showing the value of the variable
print("variable {} is of type: {} and value: {}".format("whole_number", type(whole_number), whole_number))
print("variable {} is of type: {} and value: {}".format("floating_number", type(floating_number), floating_number))
print("variable {} is of type: {} and value: {}".format("boolean_true", type(boolean_true), boolean_true))
print("variable {} is of type: {} and value: {}".format("test_text", type(test_text), test_text))
print("variable {} is of type: {} and value: {}".format("list", type(list), list))