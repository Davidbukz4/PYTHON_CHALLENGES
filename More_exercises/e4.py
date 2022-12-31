# Program prints the admission cost for a group
print("The program reads the ages of all the guests in the group. \nPress enter to indicate that there are no more guest in the group")
response = input("Enter the age of the guest: ")
total=0

while response != '':
    if int(response) >= 0:
        #response = ""
        x = int(response)
        if x <= 2:
            total += 0
        elif x >= 3 and x <= 12:
            total += 14
            #continue
        elif x >= 65:
            total += 18
            #continue
        elif x > 12 and x < 65:
            total += 23
            #continue
        else:
            print("Invalid input.\nNumber should be positive.")
            #continue
    response = input("Enter the age of the guest: ")


print("The admission cost for the group is $%.2f" % total)