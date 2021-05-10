file=open("example.txt")
dnaStrings={}
currentHeader=""
for line in file:
    if line.startswith('>'):
        dnaStrings[line]=""
        currentHeader=line
    else:
        dnaStrings[currentHeader]=dnaStrings[currentHeader]+line
highestValue=-100000
highestString=""
for dna in dnaStrings:
    countC=dnaStrings[dna].count('C')
    countG=dnaStrings[dna].count('G')
    countA=dnaStrings[dna].count('A')
    countT=dnaStrings[dna].count('T')
    GCratio=(countC+countG)/(countA+countC+countG+countT)*100
    if GCratio >=highestValue:
        highestValue=GCratio
        highestString=dna[1:]
print(highestString)
print(highestValue)
