DNAstring="AAATGCTTACGTCG".upper()
reverseComplementDNA=""
bases={'A':'T','T':'A','G':'C','C':'G'}
for base in DNAstring:
    reverseComplementDNA+=bases[base]
reverseComplementDNA=reverseComplementDNA[::-1]
print (reverseComplementDNA)
