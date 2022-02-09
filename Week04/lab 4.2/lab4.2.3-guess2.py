# lab4.2.3-guess2.py
# This program is used to spam a user, but gives usefull hints
# author: David Burke

# the nummber to be matched
theGoldenTicket = 30

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