#Program that counts for the user

print("\tThis program counts for you")
start = None
start = int(input("\nEnter starting number: "))


while start and start != None:
    stop = int(input("Enter ending number: "))
    while stop:
        if start < stop:
            sequence = int(input("Enter the sequence to count: "))
            stop += 1
            for i in range(start, stop, sequence):
                print(i)
            stop = None
        if start > stop:
            sequence = int(input("Enter the sequence to count: "))
            stop -= 1
            for i in range(start, stop, sequence):
                print(i)
            stop = None
    start = None
    start = int(input("\nEnter starting number: "))

input("Press the enter key to exit")