'''
Morphological Parser:
        Main file
'''

import tagging
import stemmer

def correctSentence(sentence, index):
        taggedS = tagging.applyMLTag(sentence)
        word = taggedS[index][0]
        POStag = taggedS[index][1]
        stemList = stemmer.stem(word, POStag)
        #remove duplicates
        verifiedWords = []
        for s in stemList:
                tags = tagging.getTagsForWord(s)
                if len(tags)>0:
                        verifiedWords += [s]
        if len(verifiedWords==0):
                return -1
        root = verifiedWords[0]
        for w in verifiedWords:
                if len(w[0]) < len(root) and tagging.mostLikelyTag(w) != 'UNK':
                        print root
                        root = w[0]
        possibles = tagging.getWordsWithRoot(root)
                



#print mostLikelyTag("state") #NN
#print mostLikelyTag("around") #IN
