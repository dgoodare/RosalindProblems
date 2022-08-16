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
    return ''.join([DNA_ReverseComplement[n] for n in seq])