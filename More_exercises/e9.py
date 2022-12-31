# Conduct a reverse lookup on a dictionary, finding all the
# keys that map to a provided value

def reverseLookup(data, value):
    # construct a list of keys to map a value
    keys = []

    # check each key, adding it to keys if the value match
    for key in data:
        if data[key] == value:
            keys.append(key)

    # return the list of keys
    return keys

# demonstrate the reverse lookup function
def main():
    french_word = {"le" : "the", "la" : "the", "livre" : "book", "pomme" : "apple"}

    print("The french words for 'the' are: ",reverseLookup(french_word,"the"))
    print("Expected: ['le','la']")
    print()
    print("The french word for 'apple' is: ",reverseLookup(french_word,"apple"))
    print("Expected: ['pomme']")
    print()
    print("The french word for 'asdf' is: ", reverseLookup(french_word,"asdf"))
    print("Expected: []")

if __name__ == "__main__":
    main()