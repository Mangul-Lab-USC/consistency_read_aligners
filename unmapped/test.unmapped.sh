#!/bin/bash
../../../bin/bwa index reference.fasta
../../../bin/bwa mem reference.fasta reads.toy.example.short.fastq > nresults/unmapped.bwa.sam

../../../bin/bowtie-build reference.fasta reference
../../../bin/bowtie -S reference reads.toy.example.short.fastq > nresults/unmapped.bowtie.sam

../../../bin/bowtie2-build reference.fasta reference.fasta
../../../bin/bowtie2 -x reference.fasta -U reads.toy.example.short.fastq > nresults/unmapped.bowtie2.sam

/u/home/s/shahar/anaconda3/bin/lordfast --index reference.fasta
/u/home/s/shahar/anaconda3/bin/lordfast --search reference.fasta --seq reads.toy.example.short.fastq > nresults/unmapped.lordfast.sam

/u/home/s/shahar/anaconda3/bin/minimap2 -a reference.fasta reads.toy.example.short.fastq  > nresults/unmapped.minimap2.sam

/u/home/s/shahar/anaconda3/bin/rmap reads.toy.example.short.fastq -c reference.fasta -o nresults/unmapped.rmap.sam

/u/home/s/shahar/anaconda3/bin/smalt index -k 14 -s 8 reference reference.fasta
/u/home/s/shahar/anaconda3/bin/smalt map -o nresults/unmapped.smalt.sam reference reads.toy.example.short.fastq

/u/home/s/shahar/anaconda3/bin/2bwt-builder reference.fasta
/u/home/s/shahar/anaconda3/bin/soapsplice -d reference.fasta.index -1 reads.toy.example.short.fasta -o nresults/unmapped.soapsplice.sam -f2

/u/home/s/shahar/anaconda3/bin/snap-aligner index ref_1.fasta index-dir
/u/home/s/shahar/anaconda3/bin/snap-aligner single index-dir reads.toy.example.short.fastq -o nresults/unmapped.snap.sam

/u/home/s/shahar/anaconda3/bin/subread-buildindex -o reference reference.fasta
/u/home/s/shahar/anaconda3/bin/subread-align -t 1 -i reference -r reads.toy.example.fastq -o nresults/unmapped.subread.sam --SAMoutput

/u/home/s/shahar/anaconda3/bin/deSALT index reference.fasta reference.fasta
/u/home/s/shahar/anaconda3/bin/deSALT aln reference.index/reads.toy.example.fastq -o nresults/unmapped.desalt.sam

#Doesn't output SAM but why not
/u/home/s/shahar/anaconda3/bin/nucmer -p nresults/unmapped.mummer reference.fasta reads.toy.example.fasta

/u/home/s/shahar/anaconda3/bin/ngmlr -r reference.fasta -q reads.toy.example.fastq -o nresults/unmapped.ngmlr.sam

/u/home/s/shahar/anaconda3/bin/nanoblaster -C10 -r reference.fasta -i reads.toy.example.long.fastq -o nresults/unmapped.nanoblaster

/u/home/s/shahar/anaconda3/bin/graphmap align -r reference.fasta -d reads.toy.example.fastq > nresults/unmapped.graphmap.sam

/u/home/s/shahar/anaconda3/bin/mrsfast --index reference.fasta
/u/home/s/shahar/anaconda3/bin/mrsfast --search reference.fasta --seq reads.toy.example.fastq -o nresults/unmapped.mrsfast.sam

/u/home/s/shahar/anaconda3/bin/ngm -r reference.fasta -q reads.toy.example.fastq -o nresults/unmapped.ngm.sam

#Not SAM again but why not
/u/home/s/shahar/anaconda3/bin/blasr --header reference.fasta reads.toy.example.fasta > nresults/unmapped.blasr.result

/u/home/s/shahar/anaconda3/bin/razers3 -o nresults/unmapped.razers3.sam reference.fasta reads.toy.example.fasta

/u/home/s/shahar/anaconda3/bin/yaha -g reference.fasta
/u/home/s/shahar/anaconda3/bin/yaha reference.fasta -q eads.toy.example.fastq -osh nresults/unmapped.yaha.sam 

cp reference.fasta copy.fa
rm ref*
mv copy.fa reference.fasta 
