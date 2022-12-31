#program displays whether integer is evn or odd
response = input("Enter a number: ")

while response.isdigit():
    if (int(response) % 2) == 0:
        print(response,"is even")
    else:
        print(response,"is odd")
    response = input("Enter a number: ")
else:
    print("You did not enter an integer")
print("bye")