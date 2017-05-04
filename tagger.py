'''
Morphological Parser:
    Tagging Functions
'''


from nltk.corpus import brown

corpus = brown.tagged_words()

def applyMLTag(words):
        dict = {}
        output = []
        for word in words:
                if dict.has_key(word):
                        print ("found repeat word: "+word)
                        output += [(word, dict[word])]
                else:
                        print("looking up new word: "+word)
                        tag = mostLikelyTag(word)
                        dict[word] = tag
                        output += [(word, tag)]
        return output

def getTagsForWord(word):
	tags = []
	for w in corpus:
		stringWord = w[0].encode('ascii','ignore')
               	stringPOStag = w[1].encode('ascii','ignore')
               	if stringWord==word and not stringPOStag in tags:
               		tags+=[stringPOStag]
        return tags

def getWordsWithRoot(root):
	words = []
        for w in corpus:
           	stringWord = w[0].encode('ascii','ignore')
               	stringPOStag = w[1].encode('ascii','ignore')
                if root in stringWord and not w in words:
                        if not '-'  in stringWord:
                    	words += [(stringWord, stringPOStag)]
        return words

def mostLikelyTag(word):
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


