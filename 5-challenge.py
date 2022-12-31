#This program gets a message from a user and prints it out backwards

print("This program prints your message backwards")
#character = ""
message = input("Enter your message: ")
backward = ""

for i in message:
        backward = i + backward
print(backward)