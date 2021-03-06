# use two lists to track words and word frequencies
from __future__ import division
import sys

lines=[l.strip().split() for l in open(sys.argv[1]).readlines()]
word_tokens=sum([len(l) for l in lines])
counts=[]
words=[]
for l in lines:
    for w in l:
        if w not in words:
            words.append(w) # or: words=words+[w]
            counts.append(1)
        else:
            counts[words.index(w)]+=1

for i in range(len(words)):
    print words[i]+'\t'+str(counts[i]/word_tokens)

