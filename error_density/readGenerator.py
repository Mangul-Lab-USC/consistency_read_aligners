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
readLength = input("What is the length of the read that we want to see?\n")
numErrors = input("What is the maximum number of errors that we want to see?\n")
readLength = int(readLength)
numErrors = int(numErrors) + 1
# This list stores the reads as we produce them in the next step
# This for loop creates the reads. For i, a number starting at the readRangeStart mentioned,
# and going all the way to readRangeEnd + readstep. This is because we want to include the max number not stop before it.
# The reads are created and incremented in length by the readstep every step of the for loop.
seqStart = randrange(11, 8500)
seqEnd = seqStart + readLength;
reads = [reference[seqStart: seqEnd]] * numErrors
for i in range(numErrors):
    if i != 0:
        temp = list(reads[i])
        num = int(readLength / (i + 1))
        count = 0 + num
        for n in range(i):
            print(count)
            print(i)
            if temp[count] == "A":
                temp[count] = "C"
            elif temp[count] == "C":
                temp[count] = "A"
            elif temp[count] == "T":
                temp[count] = "G"
            elif temp[count] == "G":
                temp[count] = "T"
            count += num
        reads[i] = "".join(temp)

print(reads)
# This next line is to check whether a file "shortest.read.length.fasta" exists. If it does, we clear it.
fastaShortReadsClear = open("shortest.read.length.fasta", "w").close()
# This line creates a "shortest.read.length.fasta" file is it doesn't already exist. It then opens the file for writing.
fastaShortReads = open("shortest.read.length.fasta", "w+")
# This for loop writes the reads to the "shortest.read.length.fasta" file
for i in range(numErrors):
    # This is how identifiers start in fasta format
    fastaShortReads.write(">R")
    # This adds on to the identifier. We're using the format ">R(length of read)" to identify the reads.
    fastaShortReads.write(str(i))
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
for i in range(numErrors):
    # This is how identifiers start in fastq format
    fastqShortReads.write("@R")
    # This adds on to the identifier. We're using the format "@R(length of read)" to identify the reads.
    fastqShortReads.write(str(i))
    # Formatting fastq
    fastqShortReads.write("\n")
    # We write the read to the file
    fastqShortReads.write(reads[i])
    # Formatting fastq
    fastqShortReads.write("\n+\n")
    # This is usually a quality score. We will just place tildas since we have created this data.
    for z in range(readLength):
        fastqShortReads.write("~")
    # Formatting fastq
    fastqShortReads.write("\n")
# Closes the file since we're finished.
fastqShortReads.close()
# fastqSoapSplice = open("soapsplice.fastq", "w").close()
# fastqSoapSplice = open("soapsplice.fastq", "w+")
# for i in range(len(reads)):
#     if len(reads[i]) > 10:
#         # This is how identifiers start in fastq format
#         fastqSoapSplice.write("@R")
#         # This adds on to the identifier. We're using the format "@R(length of read)" to identify the reads.
#         fastqSoapSplice.write(str(len(reads[i])))
#         # Formatting fastq
#         fastqSoapSplice.write("\n")
#         # We write the read to the file
#         fastqSoapSplice.write(reads[i])
#         # Formatting fastq
#         fastqSoapSplice.write("\n+\n")
#         # This is usually a quality score. We will just place tildas since we have created this data.
#         for z in range(len(reads[i])):
#             fastqSoapSplice.write("~")
#         # Formatting fastq
#         fastqSoapSplice.write("\n")
#     else:
#         continue
# fastqSoapSplice.close()
