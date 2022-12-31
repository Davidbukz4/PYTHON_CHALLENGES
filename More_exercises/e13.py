# Create and display a bingo card

from random import randrange

NUMS_PER_LETTER = 15

def createCard():
    card = {}

    lower = 1
    upper = 1 + NUMS_PER_LETTER

    for letter in ["B","I","N","G","O"]:
        card[letter] = []
        while len(card[letter]) != 5:
            next_num = randrange(lower,upper)

            if next_num not in card[letter]:
                card[letter].append(next_num)

        lower = lower + NUMS_PER_LETTER
        upper = upper + NUMS_PER_LETTER

    return card

def displayCard(card):
    print("B I N G O")

    for i in range(5):
        for letter in ["B", "I","N","G","O"]:
            print("%2d" % card[letter][i], end="")
        print()

def main():
    card = createCard()
    displayCard(card)

if __name__ == "__main__":
    main()