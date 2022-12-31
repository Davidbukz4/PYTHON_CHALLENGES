# Challenge 5.1
#
# This program prints list of words in random order
import random
WORDS = ("OVERUSED","CLAM", "GUAM", "TAFFETA", "PYTHON")
word = random.choice(WORDS)
printed = 0
a_printed = "-" * 5
#x = random.randrange(5)
a_printed = []
print(word)
a_printed.append(word)

while printed <= 3:
        word = random.choice(WORDS)
        if word not in a_printed:
            print(word)
            a_printed.append(word)
            printed += 1
        else:
            continue
