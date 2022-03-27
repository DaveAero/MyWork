# lab8.1.1-numpyExists.py
# This program is used to deomstrate Numpy
# author: David Burke

import numpy as np

np.random.seed(1) # this is so that the "random" numbers are the same each time to make it easier to debug.

# it is a good idea to have your absolute values set into variables at the beginning of your program
minSalary= 20000
maxSalary = 80000
numberOfEntries = 10
salaries = np.random.randint(minSalary, maxSalary,numberOfEntries)
print (salaries)

salariesPlus = salaries + 5000 # this will add 5000 to each value
print(salariesPlus)

# you can also multiply
salariesMult = salaries * 1.05 # add 5% by multiplying by 1.05
print(salariesMult)

# This is a float array, here I convert it to an int array (it does a floor)
newSalaries = salariesMult.astype(int)
print(newSalaries)
