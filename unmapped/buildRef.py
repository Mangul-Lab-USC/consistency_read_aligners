# This import allows us to randomly pick a number.
from random import randrange
from Bio import SeqIO
def batch_iterator(iterator, batch_size):
    """Returns lists of length batch_size.

    This can be used on any iterator, for example to batch up
    SeqRecord objects from Bio.SeqIO.parse(...), or to batch
    Alignment objects from Bio.AlignIO.parse(...), or simply
    lines from a file handle.

    This is a generator function, and it returns lists of the
    entries from the supplied iterator.  Each list will have
    batch_size entries, although the final list may be shorter.
    """
    entry = True  # Make sure we loop once
    while entry:
        batch = []
        while len(batch) < batch_size:
            try:
                entry = next(iterator)
            except StopIteration:
                entry = None
            if entry is None:
                # End of file
                break
            batch.append(entry)
        if batch:
            yield batch
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
iterator = SeqIO.parse(open("reference.fasta"),"fasta")
for i, batch in enumerate(batch_iterator(iterator, 950)):
    nameOfFile = "ref_%i.fasta" % (i + 1)
    with open(nameOfFile, "w") as handle:
        count = SeqIO.write(batch, handle, "fasta")
    print("Wrote %i records to %s" % (count, nameOfFile))

