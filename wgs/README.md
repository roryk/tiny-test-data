# Mitocondrial reads from WGS

The reads in `mt_1.fq.gz` and `mt_2.fq.gz` comes from the normal sample of the synthetic dataset 3 of the ICGC-TCGA DREAM challenge. Reads aligning to the mitochontrion were extracted from the aligned BAM file, and converted to fastq format. The dataset is 2x101 paired illumina reads, In total 4597 read pairs. Average coverage after removing duplicate is around 110x, but varies wildly. This provides suffcient depth to test variant calling downstream. 
