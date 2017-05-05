'''
Morphological Parser:
    Tagging Functions
'''


import nGrams
bigramList = nGrams.bigramList

def applyMLTag(words):
        dict = {}
        output = []
        for word in words:
			asciiWord = word.encode('ascii', 'ignore')
			if dict.has_key(asciiWord):
				print ("found repeat word: "+asciiWord)
				output += [(asciiWord, dict[asciiWord])]
			else:
				print("looking up new word: "+asciiWord)
				tag = mostLikelyTag(asciiWord)
				dict[asciiWord] = tag
				output += [(asciiWord, tag)]
        return output

def getTagsForWord(word):
	tags = []
	for bigram in bigramList:
		stringWord = bigram[0][0].encode('ascii','ignore')
		stringPOStag = bigram[0][1].encode('ascii','ignore')
		if stringWord==word and not stringPOStag in tags:
			tags+=[stringPOStag]
        return tags

def getWordsWithRoot(root):
	words = []
	for bigram in bigramList:
		stringWord = bigram[0][0].encode('ascii','ignore')
		stringPOStag = bigram[0][1].encode('ascii','ignore')
		if root in stringWord and not (stringWord, stringPOStag) in words:
			words += [(stringWord, stringPOStag)]
	return words

def mostLikelyTag(word):
        dict = {}
        for bigram in bigramList:
                if bigram[0][0].encode('ascii', 'ignore')==word:
                        if dict.has_key(bigram[0][1].encode('ascii', 'ignore')):
                                dict[bigram[0][1].encode('ascii', 'ignore')] += 1
                        else:
                                dict[bigram[0][1].encode('ascii', 'ignore')] = 1
        key = ""
        amount = 0
        for k in dict.keys():
                if dict[k]>amount:
                        key = k
                        amount= dict[k]
        if(amount == 0):
                key = 'UNK'
        return key


