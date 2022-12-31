#Guess my number
#The computer picks a random number between 1 and 100
#The player tries to guess it and the computer lets
#the player know if the guess is too high, too low
#or right on the money
#It also set guess limit

import random

print("\tWelcome to \'Guess My Number\'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

# set the initial values
the_number = random.randint(1,100)
# the_number2 was just i too know work, i wanted to overdo
the_number2 = random.randrange(100) + 1
guess = int(input("Take a guess: "))
tries = 1

# guessing loop
if tries <= 7:
    while guess != the_number and tries != 7:
        if guess > the_number:
            print("Lower...")
        else:
            print("Higher...")

        guess = int(input("Take another guess: "))
        tries += 1
    if guess == the_number:
        print("You guessed it! The number was", the_number)
        print("And it took you", tries, "tries!\n")
    else:
        print("oops!\nYou've ran out of guesses.")

input("\n\nPress the enter key to exit.")