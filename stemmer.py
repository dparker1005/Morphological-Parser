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

prefixes = csvReader('prefixes.csv')
suffixes = csvReader('suffixes.csv')
irregulars = csvReader('irregularPastVerbs.csv')

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
#print "1"
        x = ['ize', 'ied', 'ies']
        if((word[-3:] in x) and (tagger.mostLikelyTag(word[:-3]+'y') != 'UNK')):
				result.append((word[:-3] + 'y', tagger.mostLikelyTag(word[:-3]+'y')))
#       print "2"
        if(tagger.mostLikelyTag(word) != 'UNK'):
				result.append((word, tagger.mostLikelyTag(word)))
#       print "2.5"
        if(tagger.mostLikelyTag(word[:-1]) != 'UNK' and word[-1] == word[-2]):
				result.append((word[:-1], tagger.mostLikelyTag(word[:-1])))
#       print "3"
        if(tagger.mostLikelyTag(word+'e') != 'UNK'):
				result.append((word+'e', tagger.mostLikelyTag(word+'e')))
        if(word[-1]=='e'):
                if(tagger.mostLikelyTag(word[:-1]+'ing') != 'UNK'):
                        result.append((word[:-1]+'ing', tagger.mostLikelyTag(word[:-1]+'ing')))
#       print "4"
        if(not foundAffix):
				for row in irregulars:
			#				print(word+"!")
				        if(row[1] == word or row[2] == word):
					#	        print "found match"
		        		        result.append((row[0], tagger.mostLikelyTag(row[0])))
        return result
#print stem("amuse")
#print stem("walking", "VB")

