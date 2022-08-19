from DNAToolkit import *
from utilities import coloured
import random

#create a random DNA sequence for testing
rndDNAStr = ''.join([random.choice(Nucleotides) for n in range(50)])

DNAStr = validateSeq(rndDNAStr)
RNAStr = transcription(DNAStr)

print(f'\nDNA Sequence: {coloured(DNAStr)} \n')
print(f'1. Sequence length: {len(DNAStr)}')

print(coloured(f'2. Nucleotide frequency: {sorted(countNucFrequency(DNAStr).items())} \n'))

print(f'3. DNA/RNA transcription: {coloured(RNAStr)} \n')

print(f"4. DNA string + complement + reverse complement: \n 5' {coloured(DNAStr)} 3' ")
print(f"    {''.join(['|' for c in range(len(DNAStr))])}")
print(f" 3' {coloured(reverse_complement(DNAStr)[::-1])} 5'")
print(f"Reverse complement: 5' {coloured(reverse_complement(DNAStr))} 3' \n")

print(f"5. GC Content: {gc_content(DNAStr)}%")

print(f"6. GC content in Subsection k = 5: {gc_content_subseq(DNAStr, k=5)} \n")

print(f"7. Amino acids sequence from DNA: {translate_seq(DNAStr)} \n")

print(f"8. Codon frequency (L): {codon_usage(DNAStr, 'L')}\n")