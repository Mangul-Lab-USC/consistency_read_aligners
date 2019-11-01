#!/bin/bash
cp shortest.read.length.fastq reads.toy.example.fastq
cp shortest.read.length.fasta reads.toy.example.fasta 
../../../bin/bowtie2-build reference.fasta reference.fasta 
../../../bin/bowtie2 -x reference.fasta -U reads.toy.example.fastq > nresults/bowtie2.sam
cp reference.fasta copy.fa
rm ref*
mv copy.fa reference.fasta
rm reads.toy.example.fastq
rm reads.toy.example.fasta


