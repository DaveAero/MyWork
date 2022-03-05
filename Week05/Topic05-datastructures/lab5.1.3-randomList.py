# lab5.1.3-randomList.py
# This program is to gereate and print a random list of numbers
# author: David Burke

# Load the random function
import random

#creat blank list
queue = []

# Number of entries into the list
numberOfNumbers = int(10)

# random number range
rangeTo = int(100)

# creating the random number list
for n in range(0,numberOfNumbers):
    queue.append(random.randint(0,rangeTo))

# print the queue for the user to see
print("queue is {}".format(queue))

# use a while loop to loop the removal of 1 number at a time
while len(queue) != 0:

        # the command pop(0) takes the first element out of a list
        currentNumber = queue.pop(0)
        print("current Number is {} and the queue is {}".format(currentNumber, queue))

print ("the queu is now empty")