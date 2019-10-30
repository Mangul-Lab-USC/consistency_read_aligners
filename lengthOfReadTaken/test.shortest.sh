#!/bin/bash
#Some of the tools here have been commented out to test the programs written in this file. Also, depending on where your file is located, you should change the commands to reflect their locations. 
cp shortest.read.length.fastq reads.toy.example.fastq
cp shortest.read.length.fasta reads.toy.example.fasta 

#blasr --header reference.fasta reads.toy.example.fasta > results/shortest.blasr.result

../../../bin/snap-aligner index reference.fasta index-dir
../../../bin/snap-aligner single index-dir reads.toy.example.fastq -o nresults/snap.sam

../../../bin/rmap reads.toy.example.fastq -c reference.fasta -o nresults/rmap.sam

../../../bin/segemehl.x -x reference.idx -d reference.fasta
../../../bin/segemehl.x -i reference.idx -d reference.fasta -q reads.toy.example.fasta > nresults/segemehl.sam

../../../bin/smalt index -k 14 -s 8 reference reference.fasta
../../../bin/smalt map -o nresults/smalt.sam reference reads.toy.example.fastq

#had to manually test, it cannot align a read 10 bps long
../../../bin/2bwt-builder reference.fasta
../../../bin/soapsplice -d reference.fasta.index -1 soapsplice.reads.fastq -o nresults/soapsplice -f2

../../../bin/splazers reference.fasta reads.toy.example.fasta -o nresults/splazers.result

../../../bin/subread-buildindex -o reference reference.fasta
../../../bin/subread-align -t 1 -i reference -r reads.toy.example.fastq -o nresults/subread.sam --SAMoutput

../../../bin/gmapper-ls reads.toy.example.fasta reference.fasta > nresults/shrimp.sam

../../../bin/nanoblaster -C10 -r reference.fasta -i reads.toy.example.long.fastq -o nresults/nanoblaster

../../../bin/micro_razers reference.fasta reads.toy.example.fasta -o nresults/micro_razers.sam

../../../bin/nucmer -p nresults/mummer reference.fasta reads.toy.example.fasta

../../../bin/bowtie-build reference.fasta reference
../../../bin/bowtie -S reference reads.toy.example.fastq > nresults/bowtie.sam    

../../../bin/bowtie2-build reference.fasta reference.fasta 
../../../bin/bowtie2 -x reference.fasta -U reads.toy.example.fastq > nresults/bowtie2.sam

../../../bin/bwa index reference.fasta
../../../bin/bwa mem reference.fasta reads.toy.example.fastq > nresults/bwa.sam

#erne-create --fasta reference.fasta --output-prefix ref
#erne-map --force-standard --sam --reference ref.ebh --query1 reads.toy.example.fastq --output results/shortest.erne.sam

#hisat2-build reference.fasta reference
#Can use either fasta (-f) or fastq file (-q) for reads
#hisat2 -q -x reference -U reads.toy.example.fastq > results/shortest.hisat2.sam

../../../bin/ngm -r reference.fasta -q reads.toy.example.fastq -o nresults/ngm.sam 

../../../bin/minimap2 -a reference.fasta reads.toy.example.fastq  > nresults/minimap2.sam

cp reads.toy.example.fastq reads.toy.example.fq
cp reference.fasta reference.fa
../../../bin/minialign -xont.1dsq reference.fa reads.toy.example.fq > nresults/minialign.sam

../../../bin/lastdb -uNEAR -R01 reference reference.fasta
../../../bin/lastal -Q1 reference reads.toy.example.fastq | last-split> nresults/last.maf

../../../bin/ngmlr -r reference.fasta -q reads.toy.example.fastq -o nresults/ngmlr.sam

../../../bin/lordfast --index reference.fasta
../../../bin/lordfast --search reference.fasta --seq reads.toy.example.fastq > nresults/lordfast.sam

../../../bin/graphmap align -r reference.fasta -d reads.toy.example.fastq > nresults/graphmap.sam

rm reads.toy.example.fq
cp reference.fasta copy.fa
rm ref*
mv copy.fa reference.fasta
rm reads.toy.example.fastq
rm reads.toy.example.fasta
