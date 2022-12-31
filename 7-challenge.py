#This program makes you guess what the computer has picked

WORD = ("one","two","three","four","five","six","seven")

hashed_word = ""
import random
chances = 1
check_alpha = ""

word = random.choice(WORD)
for i in range(len(word)):
    hashed_word += "*"


print("The number in words is",hashed_word, "and it has", len(word),"letters")
print("Guess the number in words")
print("You have 5 chances to ask if a letter is in the word")

print("To check if a particular letter is in the word")
while chances <= 5:
    check_letter = input("Enter the letter: ")
    for j in range(len(check_letter)):
        for k in range(len(word)):
            if check_letter[j] == word[k]:
                #check_alpha += word[k]
                print("Yes")
                #print(check_alpha)
                break

    chances += 1


print("With all these clues, can you guess the word?")
guessed_word = input("What is the word: ")
if guessed_word == word:
    print("Correct!")
else:
    print("Try again.")