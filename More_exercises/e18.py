# remove contents of a file

#read and open the input file, ensuring it was opened successfully
try:
    in_name = input("Enter the name of a python file: ")
    inf = open(in_name,"r")
except:
    print("A problem was encountered while opening the input file.")
    print("Quitting...")
    quit()

# read and open the output file ensuring that it was opened successfully
try:
    out_name = input("Enter the output file name: ")
    outf = open(out_name,"w")
except:
    print("A problem was encountered while opening the output file.")
    print("Quitting...")
    quit()

#read all the lines from the input file, process them to
# remove comments, and save the lines to a new file
try:
    for line in inf:
        #find the position of the comment character
        #(-1 if there isn't one)
        pos = line.find("#")

        #if there is a comment, then form a slice of the
        #string that excludes it, overwriting line
        if pos > -1:
            line = line[0 : pos]
            line = line + "\n"

        #write the (potentially modified) line to the file
        outf.write(line)

    #close files
    inf.close()
    outf.close()
except:
    print("A problem was encountered while processing the file.")
    print("Quitting...")
