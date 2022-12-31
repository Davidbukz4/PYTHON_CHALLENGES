# Write a Who's Your Daddy? program that lets user enter the name of a male
# and produces the name of his father. Allow the user to add, replace, and
# delete son-father pairs.

son_father = {'tom cruise':'anthony hopkins', 'boris becker':'tin tin'}
son = ''
father = ''
choice = None

while choice != "0":
    print("""\n\nWould you like to:
    0 - Exit
    1 - View the Son-Father pair
    2 - Add a Son-Father pair
    3 - Replace a Son-Father pair
    4 - Delete a Son-Father
    """)
    choice = input("Which option would you like to choose? ")
    if choice == "1":
        if son_father == {}:
            print("The database is empty right now, why don't you add some!")
            continue
        else:
            for son, father in son_father.items():
                print(son.title(), "is", father.title(), "'s son.")

    elif choice == "2":
        son = input("Who is the son? ")
        son = son.lower()
        if son in son_father:
            print("That son already exists! Try replacing the son instead.")
            continue
        father = input("Who is the father? ")
        father = father.lower()
        son_father[son] = father
        print("\n", son.title(), "is", father.title(),"\b's son.")

    elif choice == "3":
        sorf = input("Do you know the son or father?: ")
        sorf = sorf.lower()
        while sorf != "son" and sorf != "father":
            print("Sorry, please write 'son' or 'father?: ")
            sorf = input("Do you know the son or father?: ")
            sorf = sorf.lower()
        if sorf == "son":
            son = input("Who is the son? ")
            son = son.lower()
            if son in son_father.keys():
                print("This current father is", son_father[son].title())
                father = input("Who would you like to replace him with?: ")
                father = father.lower()
                son_father[son] = father
            elif son not in son_father.keys():
                print("That son doesn't exist. Why don't you try adding him?")
                continue
        if sorf == "father":
            father = input("Who is the dad? ")
            father = father.lower()
            if father in son_father.values():
                for son, dad in son_father.items():
                    if dad == father:
                        print("The current son is", son.title())
                        del son_father[son]
                        son = input("Who would you like to replace him with?: ")
                        son_father[son] = father
                        print(son.title(), " is ", father.title(), "'s son.")
                        break
            elif father not in son_father.values():
                print(father, "doesn't exist. Why don't you try adding him?")
    elif choice == "4":
        son = input("Who is the son? ")
        son = son.lower()
        if son not in son_father:
            print(son, "doesn't! Perhaps you already deleted them.")
            continue
        else:
            print(son.title(), "and", son_father[son].title(), "have been deleted.")
            del son_father[son]

    else:
        print("Sorry, that's not a valid choice.")

print("\nThanks for playing!")
input("\n\nPress the enter key to exit.")