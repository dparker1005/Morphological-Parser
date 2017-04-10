# Name: David Parker
import copy

terminals = set(['that','this','a','book','flight','meal','money','include','prefer','I','she','me','Houston','TWA','does','from','to','on','near','through', 'the'])

nonterminals = set(['S','NP','Nominal','VP','PP','Det','Noun','Verb','Pronoun','Proper-Noun','Aux','Preposition'])

grammar = {'S':[['NP','VP'],['Aux','NP','VP'],['VP']],'NP':[['Pronoun'],['Proper-Noun'],['Det','Nominal']],'Nominal':[['Noun'],['Nominal','Noun'],['Nominal','PP']],'VP':[['Verb'],['Verb','NP'],['Verb','NP','PP'],['Verb','PP'],['VP','PP']],'PP':[['Preposition','NP']],'Det':[['that','this','a', 'the']],'Noun':[['book','flight','meal','money']],'Verb':[['book','include','prefer']],'Pronoun':[['I','she','me']],'Proper-Noun':[['Houston','TWA']],'Aux':[['does']],'Preposition':[['from','to','on','near','through']]}

# This function determines whether a grammar is in Chomsky Normal Form

def InCNF(g):
    # Fill in your algorithm here
    for key in g.keys():
        gram = g[key]
        #print gram
        for rule in gram:
            if rule[0] in terminals:
                for word in rule:
                    if word not in terminals:
                        return False
            else:
                if len(rule) != 2:
                    return False
        
    return True # Placeholder

# This function takes a grammar and returns an equivalent grammar in Chomsky Normal Form

def ConvertToCNF(g):
    newGrammar = {}
    oldGrammar = dict(g)
    
    #put all nonterminals leading to terminals into newGrammar
    keysToRemove = []
    for key in oldGrammar:
        gram = oldGrammar[key]
        for rule in gram:
            if rule[0] in terminals:
                newGrammar[key] = copy.copy([rule])
                keysToRemove += [key]

    for key in keysToRemove:
        del oldGrammar[key]

#    print newGrammar
#    print oldGrammar
#    
#    print("-----------------------------------------")

    #put all nonterminal rules leading only to terminals into newGrammar
    newGrammarCopy = dict(newGrammar)
    for key in oldGrammar:
        gram = oldGrammar[key]
        rulesToRemove = []
        for rule in gram:
            if (len(rule)==1) and (rule[0] in newGrammarCopy.keys()):
                if(rule[0] in newGrammar.keys()):
                    if(key in newGrammar.keys()):
                        newGrammar[key] += copy.copy(newGrammar[rule[0]])
                    else:
                        newGrammar[key] = copy.copy(newGrammar[rule[0]])
                    rulesToRemove += [rule]
        for rule in rulesToRemove:
            oldGrammar[key].remove(rule)

#    print newGrammar
#    print oldGrammar
#
#    print("-----------------------------------------")

    #put all nonterminals leading to two nonterminals into the grammar
    keysToRemove = []
    for key in oldGrammar:
        gram = oldGrammar[key]
        rulesToRemove = []
        for rule in gram:
            if(len(rule)==2):
                if(key in newGrammar.keys()):
                    newGrammar[key]+= [rule]
                else:
                    newGrammar[key] = [rule]
                rulesToRemove += [rule]
        for rule in rulesToRemove:
            oldGrammar[key].remove(rule)
            if len(oldGrammar[key])==0:
                keysToRemove += [key]
    for key in keysToRemove:
        del oldGrammar[key]

#    print newGrammar
#    print oldGrammar
#    
#    print("-----------------------------------------")

    #put all remaining nonterminals with rules longer than 3 into the grammar
    keysToRemove = []
    keyIndex = 1
    for key in oldGrammar:
        gram = oldGrammar[key]
        rulesToRemove = []
        for rule in gram:
            if(len(rule)==3):
                newKeyName ="X"+str(keyIndex)
                #exec syntax found at http://stackoverflow.com/questions/11553721/using-a-string-variable-as-a-variable-name
                exec(newKeyName+" = ['"+rule[0]+"', '"+rule[1]+"']")
                exec("newGrammar[newKeyName] = ["+newKeyName+"]")
                if(key in newGrammar.keys()):
                    newGrammar[key]+= [[newKeyName, rule[2]]]
                else:
                    newGrammar[key] = [[newKeyName, rule[2]]]
                rulesToRemove += [rule]
                keyIndex += 1
    
        for rule in rulesToRemove:
            oldGrammar[key].remove(rule)
            if len(oldGrammar[key])==0:
                keysToRemove += [key]
    for key in keysToRemove:
        del oldGrammar[key]

#    print newGrammar
#    print oldGrammar
#    
#    print("-----------------------------------------")

    #put all complex rules with lengths equal to 1 into the grammar
    for key in oldGrammar:
        gram = oldGrammar[key]
        for rule in gram:
            if len(rule) == 1:
                for ruleToAdd in newGrammar[rule[0]]:
                    if(key in newGrammar.keys()):
                        newGrammar[key]+= [ruleToAdd]
                    else:
                        newGrammar[key] = [ruleToAdd]

    return dict(newGrammar) # Placeholder


# This function takes a grammar and a string and returns True if that grammar generates that string, False otherwise. 

def CKYRecognizer(g,s):
    if s == '':
        print("There is no sentence.")
        return False
    if not InCNF(g):
        print("Grammar is not in CNF.")
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

print InCNF(grammar) # Should return False!

newgrammar = ConvertToCNF(grammar)

print newgrammar

print InCNF(newgrammar) # Should return True!

print CKYRecognizer(newgrammar,'Book the flight through Houston') # Should return True!

# Add more tests of CKYRecognizer here.
print CKYRecognizer(grammar,'Book the flight through Houston') # Should return False due to non-CNF grammar
print CKYRecognizer(newgrammar,'Book a money through Houston') # Should return True, although wouldn't be said
print CKYRecognizer(newgrammar,'Prefer this flight through TWA') # Should return True, although wouldn't be said
print CKYRecognizer(newgrammar,'') # Check null string, should return false
print CKYRecognizer(newgrammar,'book the a flight') # Should return False
print CKYRecognizer(newgrammar,'A flight book') # Should return False
print CKYRecognizer(newgrammar,'Book') # Should return True
