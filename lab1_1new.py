import re
from scipy.spatial import distance
from collections import Counter
import math
import numpy as np


def cos(vec1, vec2):
    scalPr = 0
    modA = 0
    modB = 0
    for i in range(len(vec1)):
        scalPr += vec1[i]*vec2[i]
        modA += vec1[i]*vec1[i]
        modB += vec2[i]*vec2[i]
        z = math.sqrt(modA) * math.sqrt(modB)
    if not z:
        return 0
    else: return 1 - scalPr/z


f = open('/Users/aidausmanova/Desktop/sentences.txt', 'r')
limes = f.readlines()

myDict = {}
d = 0
n = 0

for line in limes:
    n += 1
    line = line.lower()
    words = re.split('[^a-z]', line)
    for word in words:
        if (word != ''):
            if word not in myDict:
                myDict[word] = d
                d += 1
            else: continue
Matrix = []
c = 0
for line in limes:
    words = re.split('[^a-z]', line.lower())
    nn = [0]*d
    for word in words:          
            for i in range(d):
                if (word != ''):
                    if i == myDict[word]:
                         nn[i] = nn[i] + 1
    Matrix.insert(c, nn)
    c += 1

#for sent in range(0, len(limes)):
   # Matrix.append([0 for i in myDict])
    #for line in limes[sent]:
        #w = myDict[line] 
        #Matrix[sent][w] += 1



#print Matrix
min1 = cos(Matrix[0], Matrix[1])
min2 = cos(Matrix[0], Matrix[2])
id1 = 1
id2 = 2
if min1 > min2:
    min3 = min2
    min2 = min1
    min1 = min3
    id3 = id2
    id2 = id1
    id1 = id3
for i in range(n):
    if(i != 0):
        print (cos(Matrix[0], Matrix[i]))
        if cos(Matrix[0], Matrix[i]) < min1:
            min2 = min1
            id2 = id1
            min1 = cos(Matrix[0], Matrix[i])
            id1 = i
        elif cos(Matrix[0], Matrix[i]) < min2:
            min2 = cos(Matrix[0], Matrix[i])
            id2 = i

print (id1, id2)