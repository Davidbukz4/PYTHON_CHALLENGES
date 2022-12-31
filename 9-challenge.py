# Character Creator Program
#
#The player should be given a pool of 30 points to spend on four attributes
#Strength, Health, Wisdom, Dexterity
#The player should be able to spend points from an attribute and put them back into the pool

print("""
                CHARACTER CREATOR PROGRAM
    You have 30 points in a pool to spend as you wish on the attributes:
        STRENGTH, HEALTH, WISDOM, DEXTERITY 
        If you choose to, you can then take points from an attritube and put them back
        in the pool.
        """)

attributes = {"Strength" : 0, "Health" : 0, "Wisdom" : 0, "Dexterity" : 0}
attribute_list = """
                    There are four attributes you can choose from
                    1. Strength
                    2. Health
                    3. Wisdom
                    4. Dexterity
                    """
choice_list = """
                Character Creator Program
                Which action do you want to perform?
                
                0 - Exit
                1 - Spend point(s) on attributes
                2 - Take point(s) from an attributes
                
                Press 0,1 or 2.
                """
choice = None
pool = 30

while choice != "0":
    print("Your character has the following attributes")
    for attribute, value in attributes.items():
        print("\t",attribute.title(),": \t",value)
    print("You have ",pool,"points in the pool.")
    print(choice_list)
    choice = input("Enter a choice: ")
    while choice != "0" and choice != "1" and choice != "2":
        print("Invalid choice.")
        print(choice_list)
        choice = input("Enter your choice: ")
    while choice == "1":
        if pool == 0:
            print("You don't have enough points in the pool, try adding points to the pool.")
            break
        print("You have ",pool,"points left in the pool.")
        print("Which attribute would you like to change?")
        print(attribute_list)
        attribute_to_change = input("Attribute to change: ")
        while (attribute_to_change.title() != "Strength" and
                attribute_to_change.title() != "Health" and
                attribute_to_change.title() != "Wisdom" and
                attribute_to_change.title() != "Dexterity"):
            print("This is an invalid choice.")
            print("Which attribute would you like to change?")
            print(attribute_list)
            attribute_to_change = input("Attribute to change: ")
        else:
            points = int(input("How many points would you like to spend: "))
            while points > pool:
                print("That's too many points. You have",pool, "points to spend.")
                points = int(input("How many points would you like to spend: "))
            attributes[attribute_to_change.title()] += points
            pool -= points
            print("Your attributes: ")
            for attribute,value in attributes.items():
                print(attribute,":\t",value)
            if pool == 0:
                print("You've spent all your points.")
                choice = None
                break
            another_change = input("Do you want to make another change? Enter 'Yes' or 'No': ")
            while another_change.lower() != "yes" and another_change.lower() != "no":
                print("Invalid choice.")
                another_change = input("Do you want to make another change? Enter 'Yes' or 'No': ")
            if another_change.lower() == "no":
                break
    while choice == "2":
            if pool == 30:
                print("\nSorry,you have no points in your attributes, try adding points to your attributes.")
                break
            print("Which attribute would you like to take points out of?")
            for attribute,value in attributes.items():
                print(attribute,":\t",value)
            attribute_to_change = input("Enter your choice: ")
            while (attribute_to_change.lower() != "strength" and
                    attribute_to_change.lower() != "health" and
                    attribute_to_change.lower() != "wisdom" and
                    attribute_to_change.lower() != "dexterity"):
                print("Invalid choice.")
                print("Which attribute would you like to take points out of?")
                for attribute, value in attributes.items():
                    print(attribute, ":\t", value)
                attribute_to_change = input("Enter your choice: ")
                while attributes[attribute_to_change] == 0:
                    print("You don't have any point in that attribute.")
                    print("Which attribute would you like to take points out of?")
                    for attribute, value in attributes.items():
                        print(attribute, ":\t", value)
                    attribute_to_change = input("Enter your choice: ")
            points = int(input("How many points would you like to remove?: "))
            while points > attributes[attribute_to_change.title()]:
                print("That's too much points. You only have",attributes[attribute_to_change.title()], "points in", attribute_to_change)
                points = input("How many points would you like to remove?: ")
            print("OK!")
            pool += points
            attributes[attribute_to_change.title()] -= points
            for attribute, value in attributes.items():
                print(attribute, ":\t", value)
            print("You now have ",pool,"points in your pool")
            another_change = input("Do you want to make another change? Enter 'Yes' or 'No': ")
            while another_change.lower() != "yes" and another_change.lower() != "no":
                print("Invalid choice.")
                another_change = input("Do you want to make another change? Enter 'Yes' or 'No': ")
            if another_change.lower() == "no":
                break
print("\nGoodbye")
input("\n\nPress the enter key to exit.")