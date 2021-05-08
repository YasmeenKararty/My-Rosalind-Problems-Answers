inputFile = open("input.txt",'r')
lines=inputFile.readlines()
outputFile = open('output.txt','w')
currentLineIndex=1
for line in lines:
    if currentLineIndex%2==0:
        outputFile.write(line)
    currentLineIndex=currentLineIndex+1
inputFile.close()
outputFile.close()
