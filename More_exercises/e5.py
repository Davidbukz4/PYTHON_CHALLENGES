# This program implements caesar cipher

message = input("Enter a message: ")
shift = int(input("Enter a number to shift character: "))

new_message = ""

for ch in message:
    if ch >= "a" and ch <= "z":
        position = ord(ch) - ord("a")
        position = (position + shift) % 26
        new_char = chr(position + ord("a"))
        new_message += new_char
    elif ch >= "A" and ch <= "Z":
        position = ord(ch) - ord("A")
        position = (position + shift) % 26
        new_char = chr(position + ord("A"))
        new_message += new_char
    elif ch >= "!" and ch <= "@":
        position = ord(ch) - ord("!")
        position = (position + shift) % 32
        new_char = chr(position + ord("!"))
        new_message += new_char
    elif ch >= "[" and ch <= "`":
        position = ord(ch) - ord("[")
        position = (position + shift) % 6
        new_char = chr(position + ord("["))
        new_message += new_char
    elif ch >= "{" and ch <= "~":
        position = ord(ch) - ord("{")
        position = (position + shift) % 6
        new_char = chr(position + ord("{"))
        new_message += new_char
    else:
        new_message += ch
print("The shifted message is now",new_message)