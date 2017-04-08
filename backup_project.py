import nltk
#from nltk.book import *
from nltk.corpus import brown
from nltk.stem.lancaster import LancasterStemmer
#import pyparsing?


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

def corpusToDict(corpus):
        #returns a dictionary of all the words in the input corpus where:
                #each entry's key = "word&POStag"
                #each entry's value = number of times it appears in corpus
        #corpus = array of tuples
        #a.encode('ascii','ignore') unicode to str
        #each key is: "word&POStag"
        dict = {}
        for wordTuple in corpus:
                word = wordTuple[0].encode('ascii', 'ignore')
                POStag = wordTuple[1].encode('ascii', 'ignore')
                key = word + '&' + POStag
                if dict.has_key(key):
                        dict.[key] += 1
                else:
                        dict[key] = 1
        return dict

def findRoots(dictionary):
        #searches through input dictionary and returns dictionary of
        #root words
        dict = {}
        for key in dictionary:
                word = ''
                POStag = ''
                for i in range(0, len(key)):
                        if key[i] == '&':
                                word = key[0:i]
                                POStag = key[i+1:len(key)]
                
                                

#Grab a corpus, go through each word and throw them in a dictionary
#where each key is: "word&POS". Whenever we encounter a word we
#already found, increment its counter by 1. After, we iterate through the
#dictionary and compare current entry to next entry, then the next, then...
#asking if current entry is in other entry and visa versa.

#print mostLikelyTag("state") #NN
#print mostLikelyTag("around") #IN
print brown.tagged_words()
