#Guess my number
#The computer picks a random number between 1 and 100
#The player tries to guess it and the computer lets
#the player know if the guess is too high, too low
#or right on the money

import random

print("\tWelcome to \'Guess My Number\'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

# set the initial values

#the_number2 = random.randrange(100) + 1
the_number = int(input("What number do you have in mind: "))
tries = 1
guess = 0
high = 100
low = 1

# guessing loop
while not guess:
    reply = ""
    guess = random.randint(low, high)
    while guess != the_number:
        print("Let me guess",guess,"?")
        reply = input("Nop!\nShould i go \'higher\' or \'lower\'?")
        if reply == "higher":
            low = guess
            guess = random.randint(low,high)
            tries += 1
        if reply == "lower":
            high = guess
            guess = random.randint(low,high)
            tries += 1

print("I guessed right! The number was", guess)
print("And it took me", tries, "tries!\n")

input("\n\nPress the enter key to exit.")