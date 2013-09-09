import glob
from collections import Counter as C

#import sys

files= glob.glob('toydata/*/*.txt')
c=C()
for f in files:
    c+=C(open(f).read().strip().split())
#print c

for i in range(len(files)):
    folder=files[i].split("/")[2]

print folder

