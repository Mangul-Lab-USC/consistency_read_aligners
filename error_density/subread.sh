#/bin/bash
cp shortest.read.length.fastq reads.toy.example.fastq
cp shortest.read.length.fasta reads.toy.example.fasta 
../../../bin/subread-buildindex -o ref_1 ref_1.fasta
../../../bin/subread-align -t 1 -i ref_1 -r reads.toy.example.fastq -o nresults/subread.sam --SAMoutput
cp reference.fasta copy.fa
rm ref*
mv copy.fa reference.fasta
rm reads.toy.example.fastq
rm reads.toy.example.fasta
