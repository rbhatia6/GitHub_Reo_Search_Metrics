import csv
import math
import numpy as np
import pandas as pd
from operator import itemgetter


dictCnt = {}
repoCnt = {}
dictts = {}

with open('page-views.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV:
        ts = int(row[0])
        searchterm = row[1]
        referrer = row[2]
        cid = row[3]

        if not referrer:
            if not dictCnt.get(searchterm):
                dictCnt[searchterm.lower()] = 1
                dictts[searchterm.lower()] = [ts]
            else:
                dictCnt[searchterm] += 1
                dictts[searchterm].append(ts)
        else:
            if not repoCnt.get(referrer):
                repoCnt[referrer] = [searchterm]
            else:
                repoCnt[referrer].append(searchterm)
            dictts[referrer.lower()].append(ts)

print("\n\nTop 5 most frequently issued queries = \n {}".format(sorted(dictCnt.items(), key=itemgetter(1), reverse=True)[:5]))

repoCntFin = {}
for k,v in repoCnt.items():
    repoCntFin[k] = len(v)

print("\n\nTop 5 queries in terms of the total number of results clicked = \n {}".format(sorted(repoCntFin.items(), key=itemgetter(1), reverse=True)[:5]))

dicttsFin = {}
for k,v in dictts.items():
    dicttsFin[k] = max(v) - min(v)

count = _sum = 0
for k, v in dicttsFin.items():
    count += 1
    _sum += v
    print("k = {}, v = {}".format(k, v))

print("\n\nAverage length of a search session = {} sec. \n".format(_sum/count))
        
min1  = min(dicttsFin.values())
max1  = max(dicttsFin.values())

print("min = {}, max = {}".format(min1, max1))

buckets = 10

range1 = max1 - min1

bsize = range1 / buckets

hm = {}
for i in range(buckets):
    hm[i] = 0

for k, v in dicttsFin.items():
    buck = math.floor(((v - min1)/bsize))
    if buck == buckets: 
        buck = buckets-1 

    if hm.get(buck):
        hm[buck] += 1
    else:
        hm[buck] = 1

for k, v in sorted(hm.items()):
    outstr = "{}"
    for i in range(v):
        outstr = outstr + " *"
    print(outstr.format(k))
