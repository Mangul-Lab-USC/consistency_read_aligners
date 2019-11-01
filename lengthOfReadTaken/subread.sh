#/bin/bash
../../../bin/subread-buildindex -o referencesub referencesub.fasta
../../../bin/subread-align -t 1 -i referencesub -r subread.fastq -o nresults/subread.sam --SAMoutput
cp reference.fasta copy.fa
rm ref*
mv copy.fa referencesub.fasta
