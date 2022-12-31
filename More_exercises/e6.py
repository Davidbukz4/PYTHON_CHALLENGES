# Lists
# Sorts a list according to ascending order

#start with an empty list
data = []

num = int(input("Enter an integer (0 to quit): "))

while num != 0:
    data.append(num)
    num = int(input("Enter an integer (0 to quit): "))

# sorts data from lowest to highest
data.sort()
# data.sort(reverse=True)   to sort from highest to lowest

for num in data:
    print(num,end="\n")
