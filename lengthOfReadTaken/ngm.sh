#!/bin/bash
cp shortest.read.length.fastq reads.toy.example.fastq
cp shortest.read.length.fasta reads.toy.example.fasta 
cp reference.fasta copy.fa
../../../bin/ngm -r reference.fasta -q reads.toy.example.fastq -o nresults/ngm.sam 
rm ref*
mv copy.fa reference.fasta
rm reads.toy.example.fastq
rm reads.toy.example.fasta
