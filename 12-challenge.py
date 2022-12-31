# Trivia Challenge
# Trivia game that reads a plain text file

import sys

def open_file(file_name, mode):
    """Open a file."""
    try:
        the_file = open(file_name,mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    #line = line.replace("\'","\'")
    return line

def next_block(the_file):
    """Return the next block of data from the trivia file."""
    category = next_line(the_file)

    question = next_line(the_file)

    answers = []
    for i in range(4):
        answers.append(next_line(the_file))

    point = next_line(the_file)

    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    explanation = next_line(the_file)

    return category, question, answers, point, correct, explanation

def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to Trivia Challenge!\n")
    print("\t\t",title, "\n")

def high_scores(score):
    import pickle, shelve
    """Records player's name and score if the score is high enough"""
    high_score = open("high_scores_pickle.dat", "rb")
    high_scores = pickle.load(high_score)
    high_score.close()
    high_scores.sort(reverse=True)
    win = score
    got_a_high_score = False
    for scores in high_scores:
        (score,name) = scores
        if win >= int(score):
            got_a_high_score=True
            name=input("You've got a high score! What's your name? ")
            print("Well done ",name,"! Your score is: ",win, "!",end="")
            high_scores.sort()
            high_scores.pop(0)
            high_scores.append((win,name))
            high_scores.sort(reverse=True)
            high_score = open("high_scores_pickle.dat","wb")
            pickle.dump(high_scores,high_score)
            break
    if got_a_high_score == False:
        print("Sorry, you didn't get a high score, better luck next time!")
    high_score.close()

def main():
    trivia_file = open_file("trivia1.txt","r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    # get first block
    category, question, answers, point, correct, explanation = next_block(trivia_file)
    while category:
        #ask a question
        print(category)
        print(question)
        for i in range(4):
            print("\t", i+1, "-", answers[i])

        #get answer
        answer = input("What's your answer?: ")
        if answer == correct:
            print("\nRight!",end=" ")
            point = int(point)
            score += point
        else:
            print("\nWrong.",end=" ")
        print(explanation)
        print("Score:", score, "\n\n")

        #get next block
        category, question, answers, point, correct, explanation = next_block(trivia_file)

    high_scores(score)
    trivia_file.close()

    print("That was the last question!")
    print("Your final score is",score)

main()
input("\n\nPress the enter key to exit.")