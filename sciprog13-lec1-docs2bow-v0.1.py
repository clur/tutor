from __future__ import division
import glob, sys, math
from collections import Counter as C

files=glob.glob("toydata/*/*.txt")

c=C()
for f in files:
    c+=C(open(f).read().split())
 
def get_idf(w,docs):
    count=0
    for d in docs:
        if w in open(d).read():
            count+=1
    return len(docs)/count+1
        
dataset=[]

for f in files:
    doc=open(f).read().split()
    representation=[]
    for w in c:
        if w in doc:
            tf=doc.count(w)/len(doc)
            idf=get_idf(w,files)
            representation.append(str(tf*math.log(idf)))
        else:
            representation.append('0')
    dataset.append(representation)


# add class labels
for i in range(len(files)):
    folder=files[i].split("/")[-2]
    print "\t".join([folder]+(dataset[i]))
    print

