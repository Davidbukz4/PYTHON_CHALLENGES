# Redact a text file

#Get the name of the input file and open it
inf_name = input("Enter the name of the text file to redact: ")
inf = open(inf_name,"r")

#Get the name of the sensitive words file and open it
sen_name = input("Enter the name of the sensitive words file: ")
sen = open(sen_name,"r")

#Load all of the sensitive words into a list
words = []
line = sen.readline()
while line != "":
    line = line.rstrip()
    words.append(line)

    line = sen.readline()

sen.close()

#Get the name of the output file and open it
outf_name = input("Enter the name for the new redacted file: ")
outf = open(outf_name,"w")

#Read each line from the input file. Replace all sensitive
#words with asterisks. Then write the line to the output file.
line = inf.readline()
while line != "":
    #Check for and replace each sensitive word. Use a number of asterisks
    #that matches the number of letters in the word
    for word in words:
        line = line.replace(word,"*" * len(word))
    #write the modified line to the output file
    outf.write(line)
    #read the next line from the input file
    line = inf.readline()
#close the input and output files
inf.close()
outf.close()