#Word Jumble
#
#The computer picks a random word and then "jumbles" it
#The player has to guess the original word

import random
#initialize tries to 1
tries = 1
#creates a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
HINT = ("The language you're using to write",
        "To mix something up",
        "Not difficult",
        "Not easy",
        "What you provide when asked a question",
        "Instrument with wooden bars")

#pick one word randomly from the sequence

word = random.choice(WORDS)

#create a variable to use later to see if the gue is correct
correct = word

for real_no in range(len(WORDS)):
    if word == WORDS[real_no]:
        #i = index_no
        break

#create a jumbled version of the word
jumble = ""

while word:
    position = random.randrange(len(word))
    #takes the letter randomly and forms a new word
    jumble += word[position]
    #removes the letter that's assigned to jumble
    word = word[:position] + word[(position + 1):]

#start the game
print("""
\tWelcome to Word Jumble!

Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
""")
print("The jumble is:",jumble)

guess = input("\nYour guess: ")
while guess != correct and guess != "":
    print("Sorry, that's not it.")
    if tries > 2 and tries <= 3:
        give_hint = input("Do you want hint? y or n: ")
        if give_hint.lower() == "y" or give_hint.lower() == "yes":
            print("Hint: ",HINT[real_no])

    guess = input("Your guess: ")
    tries += 1

if guess == correct:
    print("That's it! You guessed it!\n")
    print("With a total number of ",tries,"trial(s)")

print("Thanks for playing.")