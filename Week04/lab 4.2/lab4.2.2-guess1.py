# lab4.2.2-guess1.py
# This program is used to spam a user
# author: David Burke

# the nummber to be matched
theGoldenTicket = 30

# prompt the user to enter a number
guess = int(input("Please guess a number:"))

# logic test and let the spam begin
while guess != theGoldenTicket:
    print("Wrong!")
    guess = int(input("Please guess again:"))

print("Well done! Yes the number was", theGoldenTicket)