#!/bin/bash
cp shortest.read.length.fastq reads.toy.example.fastq
cp shortest.read.length.fasta reads.toy.example.fasta 
../../../bin/smalt index -k 14 -s 8 reference reference.fasta
../../../bin/smalt map -o nresults/smalt.sam reference reads.toy.example.fastq
cp reference.fasta copy.fa
rm ref*
mv copy.fa reference.fasta
rm reads.toy.example.fastq
rm reads.toy.example.fasta
