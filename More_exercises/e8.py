def allSublists(data):
    sublists = [[]]

    for length in range(1, len(data) + 1):
        for i in range(0, len(data) + 1):
            sublists.append(data[i : i + length])

    return sublists

def main():
    print("The sublists are [] are: ")
    print(all([]))

    print("The sublists of [1] are: ")
    print(allSublists([1]))

    print("The sublists of [1,2] are: ")
    print(allSublists([1,2]))

    print("The sublists of [1,2,3] are: ")
    print(allSublists([1,2,3]))

    print("The sublists of [1,2,3,4] are: ")
    print(allSublists([1,2,3,4]))

main()