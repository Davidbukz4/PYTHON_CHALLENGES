# concatenate multiple files
import sys

if len(sys.argv) == 1:
    print("You must provide at least one file name.")
    quit()

#process all the files provided on the command line
for i in range(1, len(sys.argv)):
    fname = sys.argv[i]
    try:
        #open the current file for reading
        inf = open(fname,"r")

        #display the file
        for line in inf:
            print(line,end="")

        #close the file
        inf.close()

    except:
        print("Couldn't open/display", fname)