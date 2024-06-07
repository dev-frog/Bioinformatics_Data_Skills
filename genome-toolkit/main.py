from genome_toolkit import GenomeToolKit

gt = GenomeToolKit()

sequence = "AATTAAATGGGCCCAAA"
k = "AA"

print(gt.kmer_count(sequence, k))