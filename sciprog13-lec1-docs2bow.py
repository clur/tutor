import glob, sys
from collections import Counter as C

files=glob.glob("toydata/*/*.txt")

#print files

# build vocabulary
c=C()
for f in files:
    c+=C(open(f).read().split())
    
print c
"""
def check_in(item,list):
    if item in list:
        return "1"
    else:
        return "0"

for f in files:
    words=open(f).read().split()
    folder=f.split("/")[-2]
    values=[check_in(w,words) for w in c]
    print " ".join([folder]+values) 
"""
