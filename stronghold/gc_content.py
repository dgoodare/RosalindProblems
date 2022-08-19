def readFile(filePath):
    """read a file and return a list of the lines from the file"""
    with open(filePath, 'r') as f:
        return [line.strip() for line in f.readlines()]

def gc_content(seq):
    """Calculate the proportion of G and C bases within a DNA/RNA sequence"""
    return round((seq.count('C') + seq.count('G')) / len(seq) * 100, 6)

# 1. read data from FASTA file
FASTAFile = readFile("RosalindProblems/test_data/gc_content.txt")
FASTADict = {}
FASTALabel = ""

# 2. clean data
for line in FASTAFile:
    if '>' in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ""
    else:
        FASTADict[FASTALabel] += line

# 3. format data
# 4. calculate gc content
RESULTDict = {key: gc_content(value) for (key, value) in FASTADict.items()}

MaxGCKey = max(RESULTDict, key=RESULTDict.get)
# 5. collect results
print(f"{MaxGCKey[1:]}\n{RESULTDict[MaxGCKey]}")