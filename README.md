# *Zea Mays* SNP Calling

We sequenced three lines of *zea mays*,  using  paired-end sequencing.  This sequencing was done by our sequencing core
and we received the data on 2013-05-10. Each variety should  have **two** sequences files, with suffixes `_R1.fastq` and
`_R2.fastq`, indicating which member of the pair it is.

## Sequencing Files

All raw  FASTQ sequences are in `data/seqs`:

```bash
file data/seqs -name "*.fastq"

```

## Quality Control Steps

After  the sequencing data was recived, our first   stage of analysis was to ensure the sequences were high quality. We
ran each of the three lines' two paired-end FASTQ files through a quality diagnostic and control pipline. Our planned
pipeline is:

1. Create base quality diagnostic graphs.
2. Create  reads for adapter sequences.
3. Trim adapter sequences.
4. Trim poor quality bases.

> Recommended trimming programs:

- Trimmomatic
- Scythe
