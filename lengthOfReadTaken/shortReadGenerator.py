# This allows us to pick random places in the reference to take reads from.
from random import randrange

# This opens the "reference.fasta" file for reading.
referenceFile = open("reference.fasta", "r")
# Just checking that we're in read mode.
if referenceFile.mode == "r":
    # We then read the information contained into a variable named reference.
    reference = referenceFile.read()
# Since we have the information we need, we can close the file.
referenceFile.close()
# These questions and inputs allows us to control the size and range of the reads.
# This takes in the beginning of the range. The length of the read we start with.
readRangeStart = input("What is the beginning of the range?\n")
# This takes in the end of the range. The maximum size we want the read to be.
readRangeEnd = input("What is the end of the range?\n")
# This takes in the intervals or difference in size between each read.
readStep = input("What is the interval?\n")
# These change the input strings into integers
readRangeStart = int(readRangeStart)
readRangeEnd = int(readRangeEnd)
readStep = int(readStep)
# This list stores the reads as we produce them in the next step
reads = []
# This for loop creates the reads. For i, a number starting at the readRangeStart mentioned,
# and going all the way to readRangeEnd + readstep. This is because we want to include the max number not stop before it.
# The reads are created and incremented in length by the readstep every step of the for loop.
for i in range(readRangeStart, (readRangeEnd + readStep), readStep):
    # This creates a starting point for the read. The 11 comes from the fact that we want to skip the identifier ">Reference".
    # The 11 to 8500 range is a good place to start the read for references longer than 100000. Yet, the number should be changed based
    # on the reference to make sure there aren't any issues accessing information that doesn't exist.
    seqStart = randrange(11, 8500)
    # The read length is going to be as long as i so we add the read length to get a end position.
    seqEnd = seqStart + i;
    # We take a substring of the reference genome to create the read using the range created in the above two lines.
    reads.append(reference[seqStart: seqEnd])
# This next line is to check whether a file "shortest.read.length.fasta" exists. If it does, we clear it.
fastaShortReadsClear = open("shortest.read.length.fasta", "w").close()
# This line creates a "shortest.read.length.fasta" file is it doesn't already exist. It then opens the file for writing.
fastaShortReads = open("shortest.read.length.fasta", "w+")
# This for loop writes the reads to the "shortest.read.length.fasta" file
for i in range(len(reads)):
    # This is how identifiers start in fasta format
    fastaShortReads.write(">R")
    # This adds on to the identifier. We're using the format ">R(length of read)" to identify the reads.
    fastaShortReads.write(str(len(reads[i])))
    # Formatting fasta
    fastaShortReads.write("\n")
    # We write the read to the file.
    fastaShortReads.write(reads[i])
    # Formatting fasta
    fastaShortReads.write("\n")
# Closes the file since we're finished.
fastaShortReads.close()
# This next line is to check whether a file "shortest.read.length.fastq" exists. If it does, we clear it.
fastqShortReadsClear = open("shortest.read.length.fastq", "w").close()
# This line creates a "shortest.read.length.fasta" file is it doesn't already exist. It then opens the file for writing.
fastqShortReads = open("shortest.read.length.fastq", "w+")
# This for loop writes the reads to the "shortest.read.length.fastq" file
for i in range(len(reads)):
    # This is how identifiers start in fastq format
    fastqShortReads.write("@R")
    # This adds on to the identifier. We're using the format "@R(length of read)" to identify the reads.
    fastqShortReads.write(str(len(reads[i])))
    # Formatting fastq
    fastqShortReads.write("\n")
    # We write the read to the file
    fastqShortReads.write(reads[i])
    # Formatting fastq
    fastqShortReads.write("\n+\n")
    # This is usually a quality score. We will just place tildas since we have created this data.
    for z in range(len(reads[i])):
        fastqShortReads.write("~")
    # Formatting fastq
    fastqShortReads.write("\n")
# Closes the file since we're finished.
fastqShortReads.close()
fastqSoapSplice = open("soapsplice.fastq", "w").close()
fastqSoapSplice = open("soapsplice.fastq", "w+")
for i in range(len(reads)):
    if len(reads[i]) > 10:
        # This is how identifiers start in fastq format
        fastqSoapSplice.write("@R")
        # This adds on to the identifier. We're using the format "@R(length of read)" to identify the reads.
        fastqSoapSplice.write(str(len(reads[i])))
        # Formatting fastq
        fastqSoapSplice.write("\n")
        # We write the read to the file
        fastqSoapSplice.write(reads[i])
        # Formatting fastq
        fastqSoapSplice.write("\n+\n")
        # This is usually a quality score. We will just place tildas since we have created this data.
        for z in range(len(reads[i])):
            fastqSoapSplice.write("~")
        # Formatting fastq
        fastqSoapSplice.write("\n")
    else:
        continue
fastqSoapSplice.close()
readsub = []
for i in range(readRangeStart, (readRangeEnd + readStep), readStep):
    # This creates a starting point for the read. The 11 comes from the fact that we want to skip the identifier ">Reference".
    # The 11 to 8500 range is a good place to start the read for references longer than 100000. Yet, the number should be changed based
    # on the reference to make sure there aren't any issues accessing information that doesn't exist.
    seqStart = randrange(11, 70)
    # The read length is going to be as long as i so we add the read length to get a end position.
    seqEnd = seqStart + i;
    # We take a substring of the reference genome to create the read using the range created in the above two lines.
    readsub.append(reference[seqStart: seqEnd])
fastqSub = open("subread.fastq", "w").close()
fastqSub = open("subread.fastq", "w+")
for i in range(len(reads)):
    if len(readsub[i]) > 10:
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



