# This import allows us to randomly pick a number.
from random import randrange

# This is the list of bases
bases = ["A", "C", "T", "G"]
# This next line is to check whether a file "reference.fasta" exists. If it does, we clear it.
referenceFile = open("reference.fasta", "w").close()
# This line creates a "reference.fasta" file is it doesn't already exist. It then opens the file for writing.
referenceFile = open("reference.fasta", "w+")
# Here we write the first line of the "reference.fasta" file which is the identifier which starts with ">"
referenceFile.write(">Reference\n")
# Then using a for loop, we write the base pairs to the file. The range controls the number of base pairs we want.
for i in range(1000000):
    # This writes the base pairs to the file. The randrange(4) produces a random number between 0 and 4.
    # We then take the base pair at that location in the bases list.
    referenceFile.write(bases[randrange(4)])
# This closes the reference file.
referenceFile.close()
