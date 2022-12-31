# This program checks for anagrams

def string_count(s):

    counts = {}

    for ch in s:
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1

    return counts

def main():
    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")

    count1 = string_count(s1)
    count2 = string_count(s2)

    if count1 == count2:
        print("Those strings are anagrams.")
    else:
        print("Those strings are not anagrams.")

main()