# Display the head of a file

import sys

NUM_LINES = 10

if len(sys.argv) != 2:
    print("You must provide the file name as a command line parameter.")
    quit()

try:
    # Open the file for reading
    inf = open(sys.argv[1],"r")

    # Read the first line from the file
    line = inf.readline()

    # keep looping until we have either read and displayed 10 lines or
    # we have reached the end of the file
    count = 0
    while count < NUM_LINES and line != "":
        # Remove the trailing newline character and count the line
        line = line.rstrip()
        count += 1

        #display the line
        print(line)

        #read the next line from the file
        line = inf.readline()

    #close the file
    inf.close()

except IOError:
    print("An error occurred while accessing the file.")