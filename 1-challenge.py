# This program flips a coin 100 times and tells you the
# number of heads and tails

import random

head = 0
tail = 0
flip = 1

while flip <= 100:
    coin_side = 0
    coin_side = random.randrange(2)
    if coin_side:
        head += 1
    else:
        tail += 1
    flip += 1
print("You flipped",head,"heads and",tail,"tails.")
