'''
Morphological Parser:
        Main file
'''

#import tagger
import stemmer

def correctSentence(sentence, index):
        taggedS = tagging.applyMLTag(sentence)
        word = taggedS[index][0]
        POStag = taggedS[index][1]
        stemList = stemmer.stem(word, POStag)
        #remove duplicates
        verifiedWords = []
        for s in stemList:
                tags = tagging.getTagsForWord(s)
                if len(tags)>0:
                        verifiedWords += [s]
        if len(verifiedWords==0):
                return -1
        root = verifiedWords[0]
        for w in verifiedWords:
                if len(w[0]) < len(root):
                        print root
                        root = w[0]
        possibles = tagging.getWordsWithRoot(root)

def fileReader():
    bigrams = []
    file = open("bigramGrammar.txt", 'r')
    content = file.readlines()
    content= [x.strip() for x in content]
    lengthOfFile = len(content)
    y=0
    for x in content:
        print(x)
        print(str(y)+"/"+str(lengthOfFile))
        y += 1
        exec("bigrams += "+x)
    print("done")
    print(len(bigrams))

fileReader()
#print mostLikelyTag("state") #NN
#print mostLikelyTag("around") #IN
