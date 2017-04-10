# Name: David Parker
import copy

#terminals = set(['that','this','a','book','flight','meal','money','include','prefer','I','she','me','Houston','TWA','does','from','to','on','near','through', 'the'])

nonterminals = set(['S','NP','Nominal','VP','PP','Det','Noun','Verb','Pronoun','Proper-Noun','Aux','Preposition'])

grammar = {'PP': [['Preposition', 'NP']], 'Noun': [[]], 'Pronoun': [[]], 'Preposition': [[]], 'Det': [[]], 'VP': [[]], ['Verb', 'NP'], ['Verb', 'PP'], ['VP', 'PP'], ['X1', 'PP']], 'NP': [[['Det', 'Nominal']], 'S': [['NP', 'VP'], ['X2', 'VP'], ['book', 'include', 'prefer'], ['Verb', 'NP'], ['Verb', 'PP'], ['VP', 'PP'], ['X1', 'PP']], 'Verb': [['book', 'include', 'prefer']], 'Proper-Noun': [['Houston', 'TWA']], 'X2': [['Aux', 'NP']], 'Aux': [['does']], 'X1': [['Verb', 'NP']], 'Nominal': [['book', 'flight', 'meal', 'money'], ['Nominal', 'Noun'], ['Nominal', 'PP']]}

# This function takes a grammar and a string and returns True if that grammar generates that string, False otherwise. 

def createGrammar(sentence):
    corpus = brown.tagged_words()
    terminals = sentence.split()
    grammar = {'S':[['NP','VP'],['Aux','NP','VP'],['VP']],'NP':[['Pronoun'],['Proper-Noun'],['Det','Nominal']],'Nominal':[['Noun'],['Nominal','Noun'],['Nominal','PP']],'VP':[['Verb'],['Verb','NP'],['Verb','NP','PP'],['Verb','PP'],['VP','PP']],'PP':[['Preposition','NP']],'Det':[[]],'Noun':[[]],'Verb':[[]],'Pronoun':[[]],'Proper-Noun':[[]],'Aux':[[]],'Preposition':[[]]}
    for w in words:
        for wordTuple in corpus:
            if w in wordTuple:
                
def CKYRecognizer(g,s):
    if s == '':
        print("There is no sentence.")
        return False
    s = s.split()
    #set up table
    table = []
    for i in range(len(s)):
        table.append([])
        for j in range(len(s)):
            table[i].append([])
    
    for x in range(0, len(s)): #loops through columns
        for key in g.keys():
            for rule in g[key]:
                for word in rule:
                    if s[x].lower()==word.lower():
                        table[x][x].append(key)
        for y in range(x-1, -1, -1): #loops through rows backwards
            tags = []
            for z in range(x-1, y-1, -1): #loops backwards through individual cells in row, check (z,y)
                rulesToFind = []
                for p1 in table[z][y]:
                    for p2 in table [x][y+1]:
                        rulesToFind.append([p1, p2])
                for ruleToFind in rulesToFind:
                    for key in g.keys():
                        for gramRule in g[key]:
                            if gramRule == ruleToFind:
                                if key not in tags:
                                    tags.append(key)
            table[x][y] = tags

    return "S" in table[len(s)-1][0]  # Placeholder

# Demonstrations

newgrammar = ConvertToCNF(grammar)

print newgrammar

print CKYRecognizer(newgrammar,'Book the flight through Houston') # Should return True!

# Add more tests of CKYRecognizer here.
print CKYRecognizer(grammar,'Book the flight through Houston') # Should return False due to non-CNF grammar
print CKYRecognizer(newgrammar,'Book a money through Houston') # Should return True, although wouldn't be said
print CKYRecognizer(newgrammar,'Prefer this flight through TWA') # Should return True, although wouldn't be said
print CKYRecognizer(newgrammar,'') # Check null string, should return false
print CKYRecognizer(newgrammar,'book the a flight') # Should return False
print CKYRecognizer(newgrammar,'A flight book') # Should return False
print CKYRecognizer(newgrammar,'Book') # Should return True
