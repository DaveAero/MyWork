# lab4.2.4-guess3.py
# This program is used to spam a user, and now its random
# author: David Burke

# import modules
import random

# generate random number
theGoldenTicket = random.randint(0,100)

# prompt the user to enter a number
guess = int(input("Please guess a number:"))

# logic test and let the spam begin
while guess != theGoldenTicket:
    
    if guess < theGoldenTicket:
         print("Too Low")

    else:
        print("Too High")

    guess = int(input("Please guess again:"))

print("Well done! Yes the number was", theGoldenTicket)