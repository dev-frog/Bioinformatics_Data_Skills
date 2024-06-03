# List of the software and there version

1. SAMTOOLS

    SAMtools is a set of utilities for interacting with and post-processing short DNA sequence read alignments in the SAM, BAM and CRAM formats, written by Heng Li. These files are generated as output by short read aligners 

    ```bash
    $ samtools --version
    samtools 1.20
    Using htslib 1.20
    Copyright (C) 2024 Genome Research Ltd.

    ```

2. bedtools: a powerful toolset for genome arithmetic

    Collectively, the bedtools utilities are a swiss-army knife of tools for a wide-range of genomics analysis tasks. The most widely-used tools enable genome arithmetic: that is, set theory on the genome. For example, bedtools allows one to intersect, merge, count, complement, and shuffle genomic intervals from multiple files in widely-used genomic file formats such as BAM, BED, GFF/GTF, VCF. While each individual tool is designed to do a relatively simple task (e.g., intersect two interval files), quite sophisticated analyses can be conducted by combining multiple bedtools operations on the UNIX command line.

    ```bash
    $ bedtools --version
    bedtools v2.31.1

    ```

3. bioawk

    Bioawk is an extension to Brian Kernighan's awk, adding the support of several common biological data formats, including optionally gzip'ed BED, GFF, SAM, VCF, FASTA/Q and TAB-delimited formats with column names

    ```bash
    $ bioawk --version
    awk version 20110810
    ```

4. seqtk

    ```bash

    seqtk --version

    ```

5. bcftools
6. bwa
7. sqlite3
8. tabix
9. bgzip