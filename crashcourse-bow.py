from __future__ import division
from collections import Counter
import sys

#lines-list of lists of words in the text files divided into lines ('\n')
lines=[l.strip().split() for l in open(sys.argv[1]).readlines()]

freq=2 

#words-vocabulary-all words in file and count of their occurences
words=Counter(open(sys.argv[1]).read().split())
print list(words.iterkeys())


dataset=[]
for l in lines:#for each line
    representation=[]#store binary representation of a line in file in list 
    for w in words:#cycle through all words in vocabulary
        if words[w]>=freq:
            if w in l: 
                representation.append(1)#if vocabulary word is in line, mark a 1
            else:
                representation.append(0)#if not, mark a 0
    dataset.append(representation)#list of lists of binary representations

print dataset


