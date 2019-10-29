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
bases = ["A", "C", "T", "G"]
mappedShortReads = []
mappedLongReads = []
unmappedShortReads = []
unmappedLongReads = []
for i in range(5):
    seqStartShort = int(randrange(11, 3000))
    seqEndShort = int(seqStartShort + 75)
    mappedShortReads.append(reference[seqStartShort: seqEndShort])
for i in range(5):
    seqStartLong = int(randrange(11, 3000))
    seqEndLong = int(seqStartLong + 1000)
    mappedLongReads.append(reference[seqStartLong: seqEndLong])
for i in range(5):
    unmappedShortRead = ""
    for j in range(1000):
        unmappedShortRead += bases[randrange(4)]
    unmappedShortReads.append(unmappedShortRead)
for i in range(5):
    unmappedLongRead = ""
    for j in range(1000):
        unmappedLongRead += bases[randrange(4)]
    unmappedLongReads.append(unmappedLongRead)
fastqFile = open("reads.toy.example.fastq", "w").close()
fastqFile = open("reads.toy.example.fastq", "w+")
for i in range(3):
    fastqFile.write("@short")
    fastqFile.write(str(i + 1))
    fastqFile.write("\n")
    fastqFile.write(mappedShortReads[i])
    fastqFile.write("\n")
    fastqFile.write("+\n")
    for j in range(75):
        fastqFile.write("I")
    fastqFile.write("\n")
for i in range(3):
    fastqFile.write("@long")
    fastqFile.write(str(i + 1))
    fastqFile.write("\n")
    fastqFile.write(mappedLongReads[i])
    fastqFile.write("\n")
    fastqFile.write("+\n")
    for j in range(1000):
        fastqFile.write("I")
    fastqFile.write("\n")
for i in range(3):
    fastqFile.write("@unmappedshort")
    fastqFile.write(str(i + 1))
    fastqFile.write("\n")
    fastqFile.write(unmappedShortReads[i])
    fastqFile.write("\n")
    fastqFile.write("+\n")
    for j in range(75):
        fastqFile.write("I")
    fastqFile.write("\n")
for i in range(3):
    fastqFile.write("@unmappedlong")
    fastqFile.write(str(i + 1))
    fastqFile.write("\n")
    fastqFile.write(unmappedLongReads[i])
    fastqFile.write("\n")
    fastqFile.write("+\n")
    for j in range(1000):
        fastqFile.write("I")
    fastqFile.write("\n")
fastqFile.close()
fastaFile = open("reads.toy.example.fasta", "w").close()
fastaFile = open("reads.toy.example.fasta", "w+")
for i in range(3):
    fastaFile.write(">short")
    fastaFile.write(str(i + 1))
    fastaFile.write("\n")
    fastaFile.write(mappedShortReads[i])
    fastaFile.write("\n")
for i in range(3):
    fastaFile.write(">long")
    fastaFile.write(str(i + 1))
    fastaFile.write("\n")
    fastaFile.write(mappedLongReads[i])
    fastaFile.write("\n")
for i in range(3):
    fastaFile.write(">unmappedshort")
    fastaFile.write(str(i + 1))
    fastaFile.write("\n")
    fastaFile.write(unmappedShortReads[i])
    fastaFile.write("\n")
for i in range(3):
    fastaFile.write(">unmappedlong")
    fastaFile.write(str(i + 1))
    fastaFile.write("\n")
    fastaFile.write(unmappedLongReads[i])
    fastaFile.write("\n")
fastaFile.close()
fastaShortFile = open("reads.toy.example.short.fasta", "w").close()
fastaShortFile = open("reads.toy.example.short.fasta", "w+")
for i in range(5):
    fastaShortFile.write(">short")
    fastaShortFile.write(str(i + 1))
    fastaShortFile.write("\n")
    fastaShortFile.write(mappedShortReads[i])
    fastaShortFile.write("\n")
for i in range(5):
    fastaShortFile.write(">unmappedshort")
    fastaShortFile.write(str(i + 1))
    fastaShortFile.write("\n")
    fastaShortFile.write(unmappedShortReads[i])
    fastaShortFile.write("\n")
fastaShortFile.close()
fastqShortFile = open("reads.toy.example.short.fasta", "w").close()
fastqShortFile = open("reads.toy.example.short.fasta", "w+")
for i in range(5):
    fastqShortFile.write("@short")
    fastqShortFile.write(str(i + 1))
    fastqShortFile.write("\n")
    fastqShortFile.write(mappedShortReads[i])
    fastqShortFile.write("\n")
    fastqShortFile.write("+\n")
    for j in range(75):
        fastqShortFile.write("I")
    fastqShortFile.write("\n")
for i in range(5):
    fastqShortFile.write("@unmappedshort")
    fastqShortFile.write(str(i + 1))
    fastqShortFile.write("\n")
    fastqShortFile.write(unmappedShortReads[i])
    fastqShortFile.write("\n")
    fastqShortFile.write("+\n")
    for j in range(75):
        fastqShortFile.write("I")
    fastqShortFile.write("\n")
fastqShortFile.close()
fastaLongFile = open("reads.toy.example.long.fasta", "w").close()
fastaLongFile = open("reads.toy.example.long.fasta", "w+")
for i in range(5):
    fastaLongFile.write(">long")
    fastaLongFile.write(str(i + 1))
    fastaLongFile.write("\n")
    fastaLongFile.write(mappedLongReads[i])
    fastaLongFile.write("\n")
for i in range(5):
    fastaLongFile.write(">unmappedlong")
    fastaLongFile.write(str(i + 1))
    fastaLongFile.write("\n")
    fastaLongFile.write(unmappedLongReads[i])
    fastaLongFile.write("\n")
fastaLongFile.close()
fastqLongFile = open("reads.toy.example.long.fasta", "w").close()
fastqLongFile = open("reads.toy.example.long.fasta", "w+")
for i in range(5):
    fastqLongFile.write("@long")
    fastqLongFile.write(str(i + 1))
    fastqLongFile.write("\n")
    fastqLongFile.write(mappedLongReads[i])
    fastqLongFile.write("\n")
    fastqLongFile.write("+\n")
    for j in range(1000):
        fastqLongFile.write("I")
    fastqLongFile.write("\n")
for i in range(5):
    fastqLongFile.write("@unmappedlong")
    fastqLongFile.write(str(i + 1))
    fastqLongFile.write("\n")
    fastqLongFile.write(unmappedLongReads[i])
    fastqLongFile.write("\n")
    fastqLongFile.write("+\n")
    for j in range(1000):
        fastqLongFile.write("I")
    fastqLongFile.write("\n")
fastqLongFile.close()
