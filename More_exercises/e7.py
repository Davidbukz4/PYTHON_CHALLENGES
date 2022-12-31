# count number in elements in a list that are greater than
# or equal to some minimum value and less than some maximum
# value
def countRange(data,mn,mx):
    count = 0
    for e in data:
        if (mn <= e < mx):
            count += 1
    return count

def main():
    data = [1,2,3,4,5,6,7,8,9,10]

    print("Counting the elements in [1...10] that are between 5 an 7...")
    print("Result: %d Expected: 2" % countRange(data,5,7))

    print("Counting the elements in [1-10] that are between -5 and 77...")
    print("Result: %d Expected: 10" % countRange(data,-5,77))

    print("Counting the elements in [1-10] that are between 12 and 17...")
    print("Result: %d Expected: 0" % countRange(data,12,17))

    print("Counting the elements in [] that are between 0 and 100...")
    print("Results: %d Expected: 0" % countRange([],0,100))

    data = [1,2,3,4,1,2,3,4]
    print("Counting the elements in [1,2,3,4,1,2,3,4] that are", \
          "between 2 and 4...")
    print("Result: %d Expected: 4" % countRange(data,2,4))

main()