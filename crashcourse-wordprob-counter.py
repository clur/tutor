# + * len() range() sys.argv open() read()/readlines() split
from __future__ import division
import sys
from collections import Counter

c=Counter(open(sys.argv[1]).read().split())
word_tokens=sum(c.itervalues())
for w in c:
    print w+'\t'+str(c[w]/word_tokens)
