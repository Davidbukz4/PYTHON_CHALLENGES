# compute the number of unique characters in a string using
# a dictionary

# read the string the user
s = input("Enter a string: ")

characters = {}
for ch in s:
    characters[ch] = True

print("That string contained",len(characters),"unique character(s).")
print(characters)