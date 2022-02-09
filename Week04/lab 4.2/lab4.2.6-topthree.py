# lab4.2.6-topthree.py
# This program is used to generate a list of random numbers and then pick the top 3
# author: David Burke

# import libaries
import random

#peramaters
howmany = 10
topPicks = 3
rangeLow = 0
rangeHigh  = 100

numbers = []

for i in range(0,10):
    numbers.append(random.randint(rangeLow,rangeHigh))
print ("{} random numbers\t {}".format(howmany, numbers))

topOnes = numbers.copy()
topOnes.sort(reverse= True)
print("The top {} are \t\t {}".format(topPicks,topOnes[0:topPicks]))