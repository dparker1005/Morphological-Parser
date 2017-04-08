import nltk
#from nltk.book import *
from nltk.corpus import brown
from text import *

def mostLikelyTag(word):
        corpus = brown.tagged_words()
        dict = {}
        for w in corpus:
                if w[0]==word:
                        if dict.has_key(w[1]):
                                dict[w[1]] += 1
                        else:
                                dict[w[1]] = 1
        key = ""
        amount = 0
        for k in dict.keys():
                if dict[k]>amount:
                        key = k
                        amount= dict[k]
        if(amount == 0):
                key = 'UNK'
        return key

def applyMLTag(words):
        dict = {}
        output = []
        for word in words:
                if dict.has_key(word):
                        print ("found repeat word "+word)
                        output += [(word, dict[word])]
                else:
                        print("looking up new word "+word)
                        tag = mostLikelyTag(word)
                        dict[word] = tag
                        output += [(word, tag)]
        return output



print mostLikelyTag("state") #NN
print mostLikelyTag("around") #IN

