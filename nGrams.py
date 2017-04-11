'''
Morphological Parser:
    nGram functions
'''

from nltk.corpus import brown

corpus = brown.tagged_words()

def corpusBigrams():
    bigrams = []
    for i in range(1, len(corpus)):
        tally = 1
        newBigram = [corpus[i-1], corpus[i], tally]
        if newBigram in bigrams: #if newBigram is already in bigram list
            for b in bigrams:
                if newBigram == b:
                    b[2] += 1 #increment bigram tally
        else:
            bigrams.append(newBigram)
    return bigrams


#corpus = [["blah", "PP"], ["tally", "NN"], ["blah", "PP"], ["tally", "NN"], ["unamused", "JJ"]]

print corpusBigrams()
            
