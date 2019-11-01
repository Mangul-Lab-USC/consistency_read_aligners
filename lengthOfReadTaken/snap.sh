#!/bin/bash
cp shortest.read.length.fastq reads.toy.example.fastq
cp shortest.read.length.fasta reads.toy.example.fasta 
../../../bin/snap-aligner index reference.fasta index-dir
../../../bin/snap-aligner single index-dir reads.toy.example.fastq -o nresults/snap.sam
cp reference.fasta copy.fa
rm ref*
mv copy.fa reference.fasta
rm reads.toy.example.fastq
rm reads.toy.example.fasta
