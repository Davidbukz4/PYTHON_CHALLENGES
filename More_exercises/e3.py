# Program tells if a letter is vowel or consonant
# Display that sometimes y can be a vowel and atimes a consonant

vowels = "aeiou"
consonant = "bcdfghjklmnpqrstvwxz"

response = input("Enter a letter: ")
if response.lower() in vowels:
    print(response," is a vowel")
elif response.lower() in consonant:
    print(response,"is a consonant.")
elif response.lower() == "y":
    print("You know sometime y is a vowel and sometimes y is a consonant.")
else:
    print("invalid input.")
