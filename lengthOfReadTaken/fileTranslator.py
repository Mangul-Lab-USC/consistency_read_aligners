# Please change this according to the directory you are currently using.
# Please revise the "files_to_parse.txt" accordingly.
list_of_files = "/u/home/s/shahar/anaconda3/research/consistency_read_aligners/lengthOfReadTaken/nresults/files.txt"
# This opens the "files_to_parse.txt", this is the list of files that we want to parse.
f = open(list_of_files, "r")
# This opens the file that we're going to write the data to.
finalFile = open("Final.txt", "w+")
readStart = input("Where does the range start?")
readEnd = input("Where does the range end?")
readStep = input("What are the intervals?")
readStart = int(readStart)
readEnd = int(readEnd)
readStep = int(readStep)
finalFile.write("Tool Name")
for i in range(readStart,readEnd,readStep):
    finalFile.write(", ")
    finalFile.write(i)
finalFile.write("\n")
# This for loop runs for each file in the list of files.
for file in f:
    # This line takes off the new line at the end of the string.
    file = file[:-1]
    # This is to visually check what files have actually been run.
    print(file)
    # This opens the current sam file to read.
    currFile = open(file, 'r')
    # Checking to see if we're in read mode.
    if currFile.mode == "r":
        # We then read the whole file line by line into a list of lines.
        lines = currFile.readlines()
    # This closes the current file so we don't have an issue when we open a new current file.
    currFile.close()
    # This just sets the flag to false for something up ahead.
    flag = False
    # For each line in the file we're going to sift through the line to get the information that we want.
    # What we want is to know whether the reads have been mapped or not mapped. A "*" means unmapped and "REFERENCE" means mapped.
    for line in lines:
        # So! We've finally gotten to the flag.
        # Essentially the flag is there to help identify the actual tool that we are using.
        # Before looking at the reads, the program will to identify what the tool they're currently looking at is.
        # Therefore, every line that it looks at, it looks for an "ID:". Currently this is flawed as many tools
        # can have multiple "ID:". Thus it is still a work in progress. (10/25/2019)
        # Yet, if it finds the ID, then we know that the reads are coming next. Thus, we take the reads after that by
        # setting the flag to be true. This will be improved.
        if line.find("ID:") != -1:
            # Splits the line string and places the pieces of that string into a list.
            lineList = line.split()
            # Writes to identity of the tool to the file.
            finalFile.write(lineList[1])
            # The famous flag
            flag = True
            # This runs if it is a line that starts with the read identifier.
        elif flag:
            # This splits the line to make a list that is easier to work with.
            lineList = line.split()
            # Currently this program is flawed (10/25/2019). I will be working to make this portion
            # format to a csv file.
            # CSV formatting
            finalFile.write(", ")
            # We then take the third item in the list which is either a "*" or a "REFERENCE" depending on
            # whether it was mapped or unmapped.
            if lineList[2] == "Reference":
                finalFile.write("1")
            else:
                finalFile.write("0")
        else:
            continue
            # Formatting
    finalFile.write("\n")
#Closes the open files
f.close()
finalFile.close()
