#!/bin/bash

bwa index reference.fasta
bwa mem reference.fasta reads.toy.example.fastq > nresults/unmapped.bwa.sam

bowtie-build reference.fasta reference
bowtie -S reference reads.toy.example.fastq > nresults/unmapped.bowtie.sam

bowtie2-build reference.fasta reference.fasta
bowtie2 -x reference.fasta -U reads.toy.example.fastq > nresults/unmapped.bowtie2.sam

lordfast --index reference.fasta
lordfast --search reference.fasta --seq reads.toy.example.fastq > nresults/unmapped.lordfast.sam

minimap2 -a reference.fasta reads.toy.example.fastq  > nresults/unmapped.minimap2.sam

rmap reads.toy.example.short.fastq -c reference.fasta -o nresults/unmapped.rmap.sam

smalt index -k 14 -s 8 reference reference.fasta
smalt map -o nresults/unmapped.smalt.sam reference reads.toy.example.fastq

2bwt-builder reference.fasta
soapsplice -d reference.fasta.index -1 reads.toy.example.fasta -o nresults/unmapped.soapsplice.sam -f2

snap-aligner index reference.fasta index-dir
snap-aligner single index-dir reads.toy.example.short.fastq -o nresults/unmapped.snap.sam

subread-buildindex -o reference reference.fasta
subread-align -t 1 -i reference -r reads.toy.example.fastq -o nresults/unmapped.subread.sam --SAMoutput

deSALT index reference.fasta reference.fasta
deSALT aln reference.index/reads.toy.example.fastq -o nresults/unmapped.desalt.sam

#Doesn't output SAM but why not
nucmer -p nresults/unmapped.mummer reference.fasta reads.toy.example.fasta

ngmlr -r reference.fasta -q reads.toy.example.fastq -o nresults/unmapped.ngmlr.sam

nanoblaster -C10 -r reference.fasta -i reads.toy.example.long.fastq -o nresults/unmapped.nanoblaster

graphmap align -r reference.fasta -d reads.toy.example.fastq > nresults/unmapped.graphmap.sam

mrsfast --index reference.fasta
mrsfast --search reference.fasta --seq reads.toy.example.fastq -o nresults/unmapped.mrsfast.sam

ngm -r reference.fasta -q reads.toy.example.fastq -o nresults/unmapped.ngm.sam

#Not SAM again but why not
blasr --header reference.fasta reads.toy.example.fasta > nresults/unmapped.blasr.result

razers3 -o nresults/unmapped.razers3.sam reference.fasta reads.toy.example.fasta

yaha -g reference.fasta
yaha reference.fasta -q eads.toy.example.fastq -osh nresults/unmapped.yaha.sam  
