#!/bin/bash
cp shortest.read.length.fastq reads.toy.example.fastq
cp shortest.read.length.fasta reads.toy.example.fasta
cp reads.toy.example.fastq reads.toy.example.fq
cp reference.fasta reference.fa
../../../bin/minialign -xont.1dsq reference.fa reads.toy.example.fq > nresults/minialign.sam
rm reads.toy.example.fq
cp reference.fasta copy.fa
rm ref*
mv copy.fa reference.fasta
rm reads.toy.example.fastq
rm reads.toy.example.fasta

