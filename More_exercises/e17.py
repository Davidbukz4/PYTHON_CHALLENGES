# sum a list of number

line = input("Enter a number: ")
total = 0


# keep reading until the user enters a blank line
while line != "":
    try:
        #convert the line to a number
        num = float(line)
        #if conversion succeeds then add it to the total and display it
        total += num
        print("The total is now",total)
    except ValueError as e:
        print(e)

    #read the next number
    line = input("Enter a number: ")

print("The grand total is",total)