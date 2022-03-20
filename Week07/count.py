# lab7.1.2-count.py
# This program is used to count how many times it has been run
# author: David Burke

import os.path

filename = "count.txt"

def readNumber():
    try:
        with open(filename) as f:
            number = int(f.read())
            return number
    except IOError:
    # this file will be created when we write back.
    # no file assumes first time running
    # ie 0 previous runs
        return 0

def writeNumber(number):
    with open(filename, "wt") as f:
        # write takes a string so we need to convert
        f.write(str(number))

if not os.path.isfile(filename):
    print ("File does not exist")
    #initialise file here
    writeNumber(0)

# main
num = readNumber()
num += 1
print ("we have run this program {} times".format(num))
writeNumber(num)