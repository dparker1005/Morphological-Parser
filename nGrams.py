'''
Morphological Parser:
    nGram functions
'''

from nltk.corpus import brown
from operator import itemgetter, attrgetter, methodcaller

corpus = brown.tagged_words()

def corpusBigrams():
    #if bigramList != []:
      #  return bigramList
    bigrams = []
    corpLen = len(corpus)
    for i in range(1, len(corpus)):
	tempStr = str(i)+"/"+str(corpLen)
	print tempStr
        tally = 1
        newBigram = [corpus[i-1], corpus[i], tally]
        #if newBigram in bigrams: #if newBigram is already in bigram list
        #    for b in bigrams:
        #        if newBigram == b:
        #            b[2] += 1 #increment bigram tally
        #else:
            #print newBigram
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

def wordToBigram(word):
    #returns bigrams that contain input word from list of bigrams
    result = []
    for b in bigramList:
        if (word in b[0]) or (word in b[1]):
            result.append(b)
    return result

#corpus = [["blah", "PP"], ["tally", "NN"], ["blah", "PP"], ["tally", "NN"], ["unamused", "JJ"]]

corpusBigrams()
print wordToBigram("amuse")
            
