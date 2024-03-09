This Snakemake workflow is designed for processing viral metatranscriptomic data, encompassing steps such as quality control of raw sequences, read assembly, database comparisons, annotation, and statistical analysis. Here are detailed explanations of each step:

Workflow Overview

Quality Control of Raw Data
The fastp tool is used to perform quality control and filtering on the raw reads, generating clean reads.
Reads Assembly
The megahit tool is employed to de-duplicate and assemble clean reads into contigs (continuous sequence fragments).
Virus Database Comparison
diamond blastx is utilized to compare the assembled contigs against a virus database.
Extraction of Virus IDs
Sequence IDs that match the virus database are extracted from the alignment results.
Filtering Sequences by ID
Based on the obtained IDs from the previous step, sequences related to viruses are selected from the contigs.
Comparison with NR Database
The filtered viral sequences are compared against the NR protein database.
Post-processing of NR Alignment Results
Sequence IDs from the NR comparison results are extracted, identifying those present exclusively in the virus database.
Further processing and merging of alignment results corresponding to these specific virus IDs are conducted.
Annotation and Statistical Analysis
Annotation information is added to potential viral sequences using a pre-prepared annotation file.
The distribution of virus families of vertebrate origin is separately quantified and visualized through pie charts.
Non-vertebrate viruses are filtered out, and the remaining vertebrate viruses' family distributions are statistically analyzed.
Extraction of Virus Family Sequences
According to the statistics of each virus family, sequence IDs corresponding to each virus family are extracted.
Relevant sequences from the assembled contigs are retrieved based on these IDs.
Usage Guide

In the directory containing the Snakemake configuration file, execute the following command to run the entire workflow:
Bash
snakemake --cores [number of available cores] --use-conda
The configuration file has a predefined list of samples called SAMPLES, which can be modified according to actual sample conditions.
In summary, this Snakemake workflow systematically handles a series of bioinformatic procedures to process viral metagenomics data, ensuring accurate identification and annotation of viral sequences, followed by comprehensive statistical analyses.
