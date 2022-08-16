from DNAToolkit import *
from utilities import coloured
import random

#create a random DNA sequence for testing
rndDNAStr = ''.join([random.choice(Nucleotides) for n in range(50)])

DNAStr = validateSeq(rndDNAStr)
RNAStr = transcription(DNAStr)

print(f'\nDNA Sequence: {coloured(DNAStr)} \n')
print(f'1. Sequence length: {len(DNAStr)}')
print(coloured(f'2. Nucleotide frequency: {sorted(countNucFrequency(DNAStr).items())}'))
print(f'3. DNA/RNA transcription: {coloured(RNAStr)}')

print(f"4. DNA string + Reverse complement: \n 5' {coloured(DNAStr)} 3' ")
print(f"    {''.join(['|' for c in range(len(DNAStr))])}")
print(f" 3' {coloured(reverse_complement(DNAStr))} 5'")