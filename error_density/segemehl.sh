#!/bin/bash
cp shortest.read.length.fastq reads.toy.example.fastq
cp shortest.read.length.fasta reads.toy.example.fasta 
../../../bin/segemehl.x -x reference.idx -d reference.fasta
../../../bin/segemehl.x -i reference.idx -d reference.fasta -q reads.toy.example.fasta > nresults/segemehl.sam
cp reference.fasta copy.fa
rm ref*
mv copy.fa reference.fasta
rm reads.toy.example.fastq
rm reads.toy.example.fasta
