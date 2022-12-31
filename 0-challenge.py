# This program displays one of five unique fortune

import random

number = random.randint(1,5)
number1 = random.randrange(5) + 1

print("\tFortune cookie program\n")

if number == 1:
    print("You will have a mansion.")
elif number == 2:
    print("You will be great.")
elif number == 3:
    print("You will be a great inventor.")
elif number == 4:
    print("You will be wealthy.")
elif number == 5:
    print("You will fulfill your dreams.")

input("\n\nPress the enter key to exit.")