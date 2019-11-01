# This allows us to pick random places in the reference to take reads from.
from random import randrange
readRangeStart = input("What is the beginning of the range?\n")
# This takes in the end of the range. The maximum size we want the read to be.
readRangeEnd = input("What is the end of the range?\n")
# This takes in the intervals or difference in size between each read.
readStep = input("What is the interval?\n")
# These change the input strings into integers
readRangeStart = int(readRangeStart)
readRangeEnd = int(readRangeEnd)
readStep = int(readStep)
readsub = []
referencesubFile = open("referencesub.fasta", "r")
# Just checking that we're in read mode.
if referencesubFile.mode == "r":
    # We then read the information contained into a variable named reference.
    referencesub = referencesubFile.read()
# Since we have the information we need, we can close the file.
referencesubFile.close()
for i in range(readRangeStart, (readRangeEnd + readStep), readStep):
    # This creates a starting point for the read. The 11 comes from the fact that we want to skip the identifier ">Reference".
    # The 11 to 8500 range is a good place to start the read for references longer than 100000. Yet, the number should be changed based
    # on the reference to make sure there aren't any issues accessing information that doesn't exist.
    seqStart = randrange(11, 70)
    # The read length is going to be as long as i so we add the read length to get a end position.
    seqEnd = seqStart + i;
    # We take a substring of the reference genome to create the read using the range created in the above two lines.
    readsub.append(referencesub[seqStart: seqEnd])
fastqSub = open("subread.fastq", "w").close()
fastqSub = open("subread.fastq", "w+")
for i in range(len(readsub)):
    if len(readsub[i]) < 800:
        # This is how identifiers start in fastq format
        fastqSub.write("@R")
        # This adds on to the identifier. We're using the format "@R(length of read)" to identify the reads.
        fastqSub.write(str(len(readsub[i])))
        # Formatting fastq
        fastqSub.write("\n")
        # We write the read to the file
        fastqSub.write(readsub[i])
        # Formatting fastq
        fastqSub.write("\n+\n")
        # This is usually a quality score. We will just place tildas since we have created this data.
        for z in range(len(readsub[i])):
            fastqSub.write("~")
        # Formatting fastq
        fastqSub.write("\n")
    else:
        continue
fastqSub.close()