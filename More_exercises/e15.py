# Display the tail of a file

import sys
NUM_LINES = 10

# Verify that exactly one command line parameter
# (in addition to the .py file) was provided
if len(sys.argv) != 2:
    print("The file name must be provided as a command line parameter.")
    quit()

try:
    #Open the file for reading
    inf = open(sys.argv[1],"r")

    #read through the file, always saving the NUM_LINES most
    #recent lines
    lines = []
    for line in inf:
        #Add the most recent line to the end of the list
        lines.append(line)
        #if we have more than NUM_LINES lines then remove
        #the oldest one
        if len(lines) > NUM_LINES:
            lines.pop(0)

    #close the file
    inf.close()

except IOError as e:
    print(e)
    quit()

#Display the last lines of the file.
for line in lines:
    print(line,end="")