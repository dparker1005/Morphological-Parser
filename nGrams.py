'''
Morphological Parser:
    nGram functions
'''

from nltk.corpus import brown

corpus = brown.tagged_words()

def corpusBigrams():
    #if bigramList != []:
      #  return bigramList
    bigrams = []
    for i in range(1, len(corpus)):
        tally = 1
        newBigram = [corpus[i-1], corpus[i], tally]
        if newBigram in bigrams: #if newBigram is already in bigram list
            for b in bigrams:
                if newBigram == b:
                    b[2] += 1 #increment bigram tally
        else:
            #print newBigram
            bigrams.append(newBigram)
    file1 = open('bigramGrammar.txt', 'w')
    for b in bigrams:
        file1.write(b)
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
            
