import nltk
import csv
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

#def corpusToDict(corpus):
 #       #returns a dictionary of all the words in the input corpus where:
 #               #each entry's key = "word&POStag"
 #               #each entry's value = number of times it appears in corpus
 #       dict = {}
 #       for wordTuple in corpus:
  #              word = wordTuple[0].encode('ascii', 'ignore')
  #              POStag = wordTuple[1].encode('ascii', 'ignore')
  #              key = word + '&' + POStag
  #              if dict.has_key(key):
  #                      dict.[key] += 1
  #              else:
  #                      dict[key] = 1
  #      return dict

def affixReader(filename):
        #reads csv file "filename" and appends affix, old POSTag
        #and new POStag to list of arrays and returns array
        affixes = []
        file1 = open(filename)
        reader = csv.reader(file1)
        bool = True
        for row in reader:
                if bool:
                        bool = False
                        continue
                affix = str(row[0])
                oldPOStag = str(row[1])
                newPOStag = str(row[2])
                affixes.append((affix, oldPOStag, newPOStag))
        return affixes

def stemmer(word, tag):
        #strips input word of all affixes and returns root
        prefixes = affixReader('prefixes.csv')
        suffixes = affixReader('suffixes.csv')
        result = []
        #bool = False
        print word
        for p in prefixes:
                if len(p[0]) >= len(word):
                        pass
                else: #if the last few characters of word == current prefix
                        #print word[:len(p[0])] 
                        if p[0] == word[:len(p[0])] and p[2] == tag:
                                print 'we won'
                                result += stemmer(word[len(p[0]):], p[1])
                                #bool = True
        for s in suffixes: #if the last few characters of word == current suffix
                print s
                if len(s[0]) >= len(word):
                        pass
                else:
                        if s[0] == word[len(word)-len(s[0]):] and s[2] == tag:
                                print "GOT 'EM"
                                result += stemmer(word[:len(word)-len(s[0])], s[1])
                                #bool = True
        result.append((word, tag))
        return result

def getTagsForWord(word):
        corpus = brown.tagged_words()
        tags = []
        for w in corpus:
                if w[0]==word and not w[1] in tags:
                        tags+=[w[1]]
        return tags

def correctSentence(sentence, index):
        taggedS = applyMLTag(sentence)
        word = taggedS[index][0]
        POStag = taggedS[index][1]
        stemList = stemmer(word, POStag)
        #remove duplicates
        verifiedWords = []
        for s in stemList:
                tags = getTagsForWord(s)
                if len(tags)>0:
                        verifiedWords += [s]
        if len(verifiedWords==0):
                return -1
        root = verifiedWords[0]
        for w in verifiedWords:
                if len(w[0]) < len(root):
                        root = w[0]
        
        #now with all the tags, gotta figure out based on sentence structure
        #whats correct POS for root word to fit grammatically in sentence
        #then use appropriate tag and append it on
        
        
        
        

#Grab a corpus, go through each word and throw them in a dictionary
#where each key is: "word&POS". Whenever we encounter a word we
#already found, increment its counter by 1. After, we iterate through the
#dictionary and compare current entry to next entry, then the next, then...
#asking if current entry is in other entry and visa versa.

#print mostLikelyTag("state") #NN
#print mostLikelyTag("around") #IN
print stemmer('nation', 'NN')
