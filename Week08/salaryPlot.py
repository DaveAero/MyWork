# lab8.1.2-plot.py
# This program is used to deomstrate plots
# author: David Burke

import numpy as np
import matplotlib.pyplot as plt
minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

# this is so that the "random" numbers are the same each time to make it easier to debug.
np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
plt.hist(salaries)
plt.show()