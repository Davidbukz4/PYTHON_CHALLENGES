# Display all the girls' and boys' names that were the
# most popular in at least one year between 1900 and 2012.

FIRST_YEAR = 1900
LAST_YEAR = 1901

def LoadAndAdd(fname,names):
    # Open the file, read the first line, and extract the name
    inf = open(fname,"r")
    line = inf.readline()
    inf.close()
    parts = line.split()
    name = parts[0]

    # Add the name to the list if it is not already present
    if name not in names:
        names.append(name)

def main():
    # create two list to store the most popular names
    girls = []
    boys = []

    #process each year in the range, reading the first line
    #out of the girl file and the boy file
    for year in range(FIRST_YEAR, LAST_YEAR + 1):
        girl_fname = str(year) + "_girlsNames.txt"
        boys_fname = str(year) + "_boysNames.txt"

        LoadAndAdd(girl_fname, girls)
        LoadAndAdd(boys_fname, boys)

    #display the lists
    print("Girls' names that reached #1:")
    for name in girls:
        print(name)
    print()
    print("Boys' names that reached #1:")
    for name in boys:
        print(name)

main()