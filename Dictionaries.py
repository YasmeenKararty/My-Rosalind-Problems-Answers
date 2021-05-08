line="We tried list and we tried dicts also we tried Zen"
words=line.split()
dictionaryOfWords ={}
for word in words:
    if word in dictionaryOfWords: #if word already exists add to its count
        dictionaryOfWords[word]=dictionaryOfWords[word]+1
    else: #if it doesn't exist add it to the dictionary with its count as 1
        dictionaryOfWords[word]=1

for key in dictionaryOfWords:
    print (key,str(dictionaryOfWords[key]))
