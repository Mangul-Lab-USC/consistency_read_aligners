#!/bin/bash
cp shortest.read.length.fastq reads.toy.example.fastq
cp shortest.read.length.fasta reads.toy.example.fasta 
../../../bin/2bwt-builder reference.fasta
../../../bin/soapsplice -d reference.fasta.index -1 soapsplice.fastq -o nresults/soapsplice -f2
cp reference.fasta copy.fa
rm ref*
mv copy.fa reference.fasta
rm reads.toy.example.fastq
rm reads.toy.example.fasta
