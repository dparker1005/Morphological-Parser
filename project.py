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
	#print str(dict)
	key = ""
	amount = 0
	for k in dict.keys():
		if dict[k]>amount:
			key = k
			amount= dict[k]
	if(amount == 0):
		key = 'UNK'
	#print word+" --> "+key
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

def bestTransform(correct, compTagged):
	bestTag = ("UNK","UNK","UNK")
	disagreements = compareTexts(correct, compTagged)
	transforms = candidateTransforms()
	#print disagreements
	for t in transforms:
		transformed = applyTransform(compTagged, t[0], t[1], t[2])
		transformDisagree = compareTexts(correct, transformed)
		#print transformDisagree
		if(transformDisagree<disagreements):
			disagreements = transformDisagree
			bestTag = t
	return bestTag

def applyTransform(text, a, b, z): # where a --> b / z
	newText = text[:]
	for index in range(len(newText)-1):
		if(newText[index][1]==z):
			if(newText[index+1][1]==a):
				newText[index+1] = (newText[index+1][0], b)
				print("Made transform")
	return newText

def candidateTransforms():
	partsOfSpeech = ["AT", "IN", "JJ", "NN", "RB", "TO", "VB"]
	transforms = []
	for x in partsOfSpeech:
		for y in partsOfSpeech:
			for z in partsOfSpeech:
				if(x!=y):
					transforms += [(x, y, z)]
	return transforms

def compareTexts(text1, text2):
	disagreements = 0;
	if(len(text1) != len(text2)):
		print("texts not the same length")
		return
	for index in range(len(text1)):
		if(text1[index][0]==text2[index][0]):
			if(text1[index][1]==text2[index][1]):
				continue
			else:
				disagreements += 1
				continue
		else:
			print("Texts are not the same.")
			return
	return disagreement

print mostLikelyTag("state") #NN
print mostLikelyTag("around") #IN

if(True): #Testing with long Brown tagset since I was not sure how to get tags for books, set to true to run
	corpus = brown.tagged_words()
	answerKey = corpus[2000:2500]
	print answerKey
	testSet = []
	for word in answerKey:
		testSet += [word[0]]
		print word[0]

	print answerKey
	print "\n\n------------------------\n\n"
	tagged = applyMLTag(testSet)
	print tagged
	print compareTexts(tagged, answerKey)
	print "\n\n-------------------------\n\n"
	bestTransform = bestTransform(answerKey, tagged)
	print bestTransform
	newTagged = applyTransform(tagged, bestTransform[0], bestTransform[1], bestTransform[2])
	numWrong = compareTexts(newTagged, answerKey)
	print numWrong
	print "\n\n------------------------\n\n"
	print newTagged
	print answerKey
	print "\n\n-------------------------\n\n" #answers to 3 questions
	print float(float(1)-(float(numWrong)/float(len(newTagged))))
	for index in range(len(answerKey)):
		if(answerKey[index][1]!= newTagged[index][1]):
			print answerKey[index][0]+" "+answerKey[index][1]+"-->"+newTagged[index][1]

	#This program determined the part of speech of about 500 words of the Brown corpus with an
	#accuracy of 90.4%.
	#Transform Used: VB-->NN/AT_

	#INCORRECT TAGS (word correctTag->tagFromProgram)
	#received VBD-->VBN
	#Ordinary NN-TL-->JJ
	#Colquitt NP-TL-->NP-HL
	#smell VB-->NN
	#to IN-->TO
	#however WRB-->RB
	#calls NNS-->VBZ
	#shot VBD-->NN
	#to IN-->TO
	#after CS-->IN
	#received VBD-->VBN
	#calls NNS-->VBZ
	#Ordinary NN-TL-->JJ
	#too RB-->QL
	#to IN-->TO
	#calls NNS-->VBZ
	#after CS-->IN
	#scheduled VBD-->VBN
	#ordinary NN-->JJ
	#made VBD-->VBN
	#real QL-->JJ
	#Austin NP-HL-->NP
	#, ,-HL-->,
	#Texas NP-HL-->NP
	#Committee NN-->NN-TL
	#Price NP-->NN
	#watered VBN-->VBD
	#considerably RB-->QL
	#since IN-->CS
	#before IN-->CS
	#on IN-TL-->IN
	#and CC-TL-->CC
	#to IN-->TO
	#taunted VBD-->VBN
	#left VBD-->VBN
	#it PPO-->PPS
	#termed VBD-->VBN
	#extremely RB-->QL
	#Aug. NP-->NP-HL
	#since IN-->CS
	#over RP-->IN
	#more AP-->QL
	#drafted VBD-->VBN
	#force VB-->NN
	#report VB-->NN
	#to IN-->TO
	#Texas NP-TL-->NP
	#keynote NN-->VB

	#If we used a different transformation template, some of these errors would be
	#fixed, but there would be more or the same amount of errors overall.

if(False): #Testing with the sample text, set to true to run
	broken = t.split()
	for index in range(len(broken)):
		if broken[index]!=t2[index][0]:
			print broken[index]






	print "\n\n----------------------\n\n"
	tagged = applyMLTag(t.split())
	print tagged
	print compareTexts(tagged, t2)
	print "\n\n-----------------------\n\n"
	bestTransform = bestTransform(t2, tagged)
	print bestTransform #NN-->VB/TO_
	newTagged = applyTransform(tagged, bestTransform[0], bestTransform[1], bestTransform[2])
	print compareTexts(newTagged, t2)

	print "\n\n-----------------------\n\n"

	print newTagged
	print t2
