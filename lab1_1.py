from collections import Counter
import pprint
import random
import numpy as np
import re
import scipy.spatial

WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
     intersec = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersec])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator)/denominator

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)


f = open('/Users/aidausmanova/Desktop/sentences.txt', 'r')
limes = f.readlines()

myDict = dict()
i=0
for line in limes:
    #sent = line.lower().split('[^a-z]', f)
    line = re.split('[^a-z]', line.lower())
    #line = line.lower().split('[^a-z]')#разделить на слова
    #txt.append(sent)
    limes[i] = filter(None, line)
    i+=1

        
#print(txt)
#a = [[c for j in range(d)]c+=1 for i in range(n)] 

d = 0
for line in limes:
	for word in line:
		if word not in myDict:#если это первое вхождение слова
			myDict[word] = d #индексация слов
			#myDict.append({word: d})
			d+=1
		else: continue
mt = []

for sent in range(0, len(limes)):
	mt.append([0 for i in myDict])

	for line in limes[sent]:
		w = myDict[line] 
		mt[sent][w] += 1

npm = np.array(mt)

#print(mt)

dist = list()
for i in range(len(limes)):
    #distance = scipy.spatial.distance.cosine(mt[0], mt[i])
    vec1 = text_to_vector(mt[0])
    vec2 = text_to_vector(mt[i])
    distance = get_cosine(vec1, vec2)
    dist.append((i, distance))



#sorted_list = sorted(dist, key=lambda tup: tup[1])

#print (sorted_list[1][0], sorted_list[2][0])
