class GenomeToolKit:
    def __init__(self):
        pass
        
    def kmer_count(self, sequence, k):
        kmers = 0
        for i in range(len(sequence) - (len(k) - 1)):
            if sequence[i:i + len(k)] == k:
                kmers += 1
        return kmers