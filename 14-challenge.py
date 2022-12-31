# Critter Caretaker
# A virtual pet to care for

class Critter(object):
    """A virtual pet"""

    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __str__(self):
        line = "Critter object\n"
        line += "Name: " + self.name + "\n"
        line += "Hunger level: " + str(self.hunger) + "\n"
        line += "Boredom level: " + str(self.boredom) + "\n"
        line += "Total unhappiness level: " + str(self.boredom + self.hunger) + "\n"
        return line

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhapiness = self.hunger + self.boredom
        if unhapiness < 5:
            m = "happy"
        elif 5 <= unhapiness <= 10:
            m = "okay"
        elif 11 <= unhapiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m

    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time()

    def eat(self, food=4):
        print("Brruppp, Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun=4):
        print("Wheee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    crit_name = input("What do you want to name your critter?: ")
    crit = Critter(crit_name)

    choice = None
    while choice != "0":
        print \
            ("""
            Critter Caretaker

            0 - Quit
            1 - Listen to your critter
            2 - Feed your critter
            3 - Play with your critter
            """)
        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Good-bye.")

        # listen to your critter
        elif choice == "1":
            crit.talk()

        # feed your critter
        elif choice == "2":
            food = int(input("How much food would you like to give? Give value "
                             "between 1 and 6: "))
            while not (food < 6 and food > 1):
                print("That's was an invalid choice.")
                food = int(input("How much food would you like to give? Give value "
                                 "between 1 and 6: "))
            crit.eat()

        # play with your critter
        elif choice == "3":
            fun = int(input("How long would you like to play? Give value "
                            "between 1 and 6: "))
            while not (fun < 6 and fun > 1):
                print("That was an invalid choice.")
                fun = int(input("How long would you like to play? Give value "
                                "between 1 and 6: "))
            crit.play()

        elif choice == "4":
            print(crit)

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")


main()

input("Press the enter key to exit.")