'''
Morphological Parser:
    Stemmer Functions
'''

import csv
import tagger

def csvReader(filename):
        #reads csv file "filename" and appends affix, old POSTag
        #and new POStag to list of arrays and returns array
        outputs = []
        file1 = open(filename)
        reader = csv.reader(file1)
        bool = True
        for row in reader:
                if bool:
                        bool = False
                        continue
                var1 = str(row[0])
                var2 = str(row[1])
                var3 = str(row[2])
                outputs.append((var1, var2, var3))
        return outputs

def isRootOfWord(root, posOfRoot, word, posOfWord):
	#print "------------"
	#print root
	#print posOfRoot
	#print word
	#print posOfWord
	#print "------------"
	possibleRoots = stem(word, posOfWord)
	for r in possibleRoots:
		if r[0] == root:
			return True
	return False


	#if ((root, posOfRoot) in possibleRoots):
	#	return True
	#return False

def stem(word, tag):
        #strips input word of all affixes and returns root
        prefixes = csvReader('prefixes.csv')
        suffixes = csvReader('suffixes.csv')
        result = []
        foundAffix = False
        for p in prefixes:
                if len(p[0]) >= len(word):
                        pass
                else: #if the last few characters of word == current prefix
                        #print word[:len(p[0])] 
                        if p[0] == word[:len(p[0])] and p[2] == tag:
                                foundAffix = True
                                result += stem(word[len(p[0]):], p[1])
                                #bool = True
        for s in suffixes: #if the last few characters of word == current suffix
                #print s
                if len(s[0]) >= len(word):
                        pass
                else:
                        if s[0] == word[len(word)-len(s[0]):] and s[2] == tag:
                                foundAffix = True
                                result += stem(word[:len(word)-len(s[0])], s[1])
                                #bool = True
		
        if(tagger.mostLikelyTag(word) != 'UNK'):
                result.append((word, tag))
        elif(tagger.mostLikelyTag(word[:-1]) != 'UNK' and word[-1] == word[-2]):
                result.append((word[:-1], tag))
        elif(tagger.mostLikelyTag(word+'e') != 'UNK'):
                result.append((word+'e', tag))
        elif(not foundAffix):
                for row in csvReader('irregularPastVerbs.csv'):
                        if(row[1] == word or row[2] == word):
                                print("GOTEM")
                                result.append((row[0], mostLikelyTag(row[0])))
        return result
#print stem("amuse")
#print stem("walking", "VB")

