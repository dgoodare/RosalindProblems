#DNA Toolkit file
import collections
from structures import *

def validateSeq(seq):
    """Check the sequence to make sure it is valid"""
    #convert to uppercase
    tmpseq = seq.upper()
    #validate
    for n in tmpseq:
        if n not in Nucleotides:
            return False
    return tmpseq


def countNucFrequency(seq):
    """Count the frequency of each nucleotide in DNA sequence"""
    return dict(collections.Counter(seq))

 
def transcription(seq):
    """Transcrtiption: th eprocess in which DNA is transcribed into RNA"""
    #replace T (thymine) with U (uracil)
    return seq.replace('T', 'U')


def reverse_complement(seq):
    """Generate reverse complement of a DNA sequence"""
    # return ''.join([DNA_ReverseComplement[n] for n in seq])[::-1]
    mapping = str.maketrans('ATCG', 'TAGC')
    return seq.translate(mapping)[::-1]


def gc_content(seq):
    """Calculate the proportion of G and C bases within a DNA/RNA sequence"""
    return round((seq.count('C') + seq.count('G')) / len(seq) * 100)


def gc_content_subseq(seq, k=20):
    """Calculate the GC content within subsequences of a DNA/RNA sequence, default subsequence size of 20"""
    result = []
    for i in range(0, len(seq) - k + 1, k):
        subseq = seq[i:i + k]
        result.append(gc_content(subseq))
    return result