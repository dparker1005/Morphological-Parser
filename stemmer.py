'''
Morphological Parser:
    Stemmer Functions
'''

import csv

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

def isRootOfWord(root, posOfRoot, word, posOfWord):
	print "------------"
	print root
	print posOfRoot
	print word
	print posOfWord
	print "------------"
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
        prefixes = affixReader('prefixes.csv')
        suffixes = affixReader('suffixes.csv')
        result = []
        #bool = False
        for p in prefixes:
                if len(p[0]) >= len(word):
                        pass
                else: #if the last few characters of word == current prefix
                        #print word[:len(p[0])] 
                        if p[0] == word[:len(p[0])] and p[2] == tag:
                                print 'we won'
                                result += stem(word[len(p[0]):], p[1])
                                #bool = True
        for s in suffixes: #if the last few characters of word == current suffix
                print s
                if len(s[0]) >= len(word):
                        pass
                else:
                        if s[0] == word[len(word)-len(s[0]):] and s[2] == tag:
                                print "GOT 'EM"
                                result += stem(word[:len(word)-len(s[0])], s[1])
                                #bool = True
        result.append((word, tag))
        return result
#print stem("amuse")
#print stem("walking", "VB")

