# Challenge 1
# This program displays one of five unique fortune

import random

number = random.randint(1,5)
number1 = random.randrange(5) + 1

print("\tFortune cookie program\n")

if number == 1:
    print("You will have a house.")
elif number == 2:
    print("You will be great.")
elif number == 3:
    print("You will be a yahoo boy.")
elif number == 4:
    print("You be senior man.")
elif number == 5:
    print("You will not come last in life.")

input("\n\nPress the enter key to exit.")