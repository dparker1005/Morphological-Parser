'''
Morphological Parser:
    nGram functions
'''

from operator import itemgetter, attrgetter, methodcaller

bigramList = []

def corpusBigrams():
	corpus = nltk.corpus.brown.tagged_words()
	bigrams = []
	corpLen = len(corpus)
	for i in range(1, len(corpus)):
		tempStr = str(i)+"/"+str(corpLen)
		print tempStr
        tally = 1
        newBigram = [corpus[i-1], corpus[i], tally]
        bigrams.append(newBigram)

	print("sorting")
	sortedBigrams = sorted(bigrams, key=itemgetter(0,1))
			
	toReturn = []
	bigramToMatch = sortedBigrams[0]
	tally = 1
	listLen = len(sortedBigrams)
	for i in range(1, len(sortedBigrams)):
		tempStr = str(i)+"/"+str(listLen)
		print(tempStr)
		if sortedBigrams[i] == bigramToMatch:
			tally += 1
		else:
			temp = bigramToMatch
			temp[2] = tally
			toReturn += [temp]
			bigramToMatch = sortedBigrams[i]
			tally = 1

	file1 = open('bigramGrammar.txt', 'w')
	for b in toReturn:
		file1.write(str(b)+"\n")
	file1.close()
	return bigrams

def fileReader():
    print("Beginning to read in file of bigams")
    bigrams = []
    file = open("bigramGrammar.txt", 'r')
    content = file.readlines()
    content= [x.strip() for x in content]
    for x in content:
        exec("bigrams += ["+x+"]")
    print("Finished reading file of bigrams")
    return bigrams


def wordToBigram(word):
    #returns bigrams that contain input word from list of bigrams
    result = []
    #print len(bigramList)
    for b in bigramList:
        if (word in b[0]) or (word in b[1]):
            result.append(b)
    return result


bigramList = fileReader()
            
