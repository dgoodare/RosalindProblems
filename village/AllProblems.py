# import this
import collections
from posixpath import split

# === Variables and Some Arithmetic ===
a = 923
b = 888
#print(f'{a}^2 + {b}^2 = {a**2 + b**2}')


# === Strings and Lists ===
firstWordStart = 84
firstWordEnd = 93

secondWordStart = 98
secondWordEnd = 103

txtStr = 'fBQPxoNFZEaOU7wXb6bpf3v4DHwcyKVPR7AL41y3MdLa0gvnzxtHqoy9dWlATwQjYTJL0pPNUXgho71b2NQNChlidoniasqpejbelliiz2OG2u217CdGpFw2UWfaIAfoQMJS4yz4zXl0SN6s7eb8kNYReEVtZ7mUKDlFANEWYj3vKS7AK.'
#print(f'{txtStr[firstWordStart:firstWordEnd + 1]} {txtStr[secondWordStart:secondWordEnd + 1]}')

# === Conditions and Loops ===
total = 0
min = 4223
max = 9058

total = sum([x for x in range(min, max + 1) if x % 2 == 1])

print(total)

# === Working with Files ===
#outputFile = []

#with open(r'C:\Users\dunca\Documents\Programming_Projects\Python\Bioinformatics\rosalind_problems\village\input.txt', 'r') as f:
    #outputFile = [line for pos, line in enumerate(f.readlines()) if pos % 2 != 0]

#with open('out.txt', 'w') as f:
    #f.write(''.join([line for line in outputFile]))


# === Dictionaries ===
string = 'When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be'
list = string.split()

dict = dict(collections.Counter(list))

for key, value in dict.items():
    print(key, value)