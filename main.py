'''
Morphological Parser:
        Main file
'''

import tagger
import stemmer
import nGrams
import csv

def correctSentence(sentence, index):
        taggedS = tagger.applyMLTag(sentence)
        word = taggedS[index][0]
        POStag = taggedS[index][1]
        stemList = stemmer.stem(word, POStag)
        #remove duplicates
        verifiedWords = []
        for s in stemList:
			#print("found stem "+str(s))
                tags = tagger.getTagsForWord(s[0])
                if len(tags)>0:
					#print("stem added")
                        verifiedWords += [s]
	#at this point, verifiedWords should contain only real words
        if len(verifiedWords)==0:
			#print("No verified words.")
                return -1

        replacementWord = ""
        #print "Entering while loop"
        while(replacementWord == "" and len(verifiedWords)>0):
                #find the shortest word/root
                root = verifiedWords[0]
                for w in verifiedWords:
                        if len(w[0]) < len(root):
                                #print root
                                root = w
						#print("shortest word is "+str(root))
                        #possibles should contain all words that can contain the root
                        possibles = tagger.getWordsWithRoot(root[0])
                        if(root[0][-1]=='e'):
                                possibles += tagger.getWordsWithRoot(root[0][:-1])
                        elif(root[0][-1]=='y'):
                                possibles += tagger.getWordsWithRoot(root[0][:-1] + 'i')
                        for row in stemmer.csvReader("irregularPastVerbs.csv"):
                                if(row[0] == root[0]):
                                        possibles += tagger.getWordsWithRoot(row[1])
                                        possibles += tagger.getWordsWithRoot(row[2])

#print("possibles for "+str(root)+" are "+str(possibles))
                        #actualPossibles should contain all words that can be stemmed to the root
                        actualPossibles = []	
                        for word in possibles:
                                if (stemmer.isRootOfWord(root[0], root[1], word[0], word[1])):
                                        actualPossibles += [word]
				#print("actual possibles for "+str(root)+" are "+str(actualPossibles))
                        prevWord = ""
                        if index>0:
                                prevWord = sentence[index-1]
                        nextWord = ""
                        if index<len(sentence)-1:
                                nextWord = sentence[index+1]
                        replacementWord = MLWordUsingBigrams(prevWord, nextWord, actualPossibles)
						#print("replacement word found for root "+str(root)+" is "+replacementWord)
                        verifiedWords.remove(root)
                if(len(verifiedWords)==0 and replacementWord == ""):
						#print("No good replacements found. Cry now.")
                        return -1
				#print("We highly reccomend that you replace your word with "+replacementWord)
				#print("Your sentence would then become:")
                sentence[index] = replacementWord
                newSentence = ""
                for w in sentence:
                        newSentence += (w+" ")
                print newSentence
                return sentence
	


def MLWordUsingBigrams(prevWord, nextWord, possibles):
	#first word case, middle word case, last word case
	MLword = ""	
	grandTally = 0
	for p in possibles:  #p = (word, tag)
		prevTally = 0
		nextTally = 0
		bigrams = nGrams.wordToBigram(p[0])
		for b in bigrams:  #b = [(word, tag), (word, tag), tally]
			#print p
			#print b
			t1 = (b[0][0].encode('ascii', 'ignore'), b[0][1].encode('ascii', 'ignore'))
			t2 = (b[1][0].encode('ascii', 'ignore'), b[1][1].encode('ascii', 'ignore'))
			#print prevTuple
			#print nextTuple


			if [t1[0], t2[0], t1[1]] == [p[0], nextWord, p[1]] and nextTally < b[2]:
				nextTally = b[2]
			elif [t1[0], t2[0], t2[1]] == [prevWord, p[0], p[1]] and prevTally < b[2]:
				prevTally = b[2]
		#print ("===========" + p[0] + "===========")
		#print ("prevTally is: " + str(prevTally))
		#print ("nextTally is: " + str(nextTally))
		if prevTally*nextTally>grandTally:
			MLword = p[0]
			grandTally = prevTally*nextTally
	#print("THIS IS OUR WINNNER!!!!!! --> "+MLword)
	return MLword

def evaluate(filename):
	testData = []
	file1 = open(filename)
	reader = csv.reader(file1)
	for row in reader:
		words = row[0].split()
		index = row[1]
		answer = row[2]
		testData.append([words, index, answer])
	count = 0.0
	for t in testData:
		print "Correcting "+str(t[0])
		correctedSent = correctSentence(t[0], int(t[1]))
		print "Corrected form is "+str(correctedSent)
		if correctedSent[t[1]] == t[2]:
			print "This is the correct form of the sentence."
			count += 1
		else:
			print "This is not the correct form of the sentence. We wanted "+t[2]+" instead of "+correctSent[t[1]]
		print "\n--------------------\n"
	print ('Based on the test data, out of ' + str(len(testData)) + ' cases, attained a ' + str(count/len(testData)) + '% accuracy rate.')

evaluate("testSentences.csv")
