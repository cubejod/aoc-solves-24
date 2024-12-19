import copy
import heapq
import math
from collections import Counter, deque
import itertools
import re
d = open("day19input.txt").read().strip()
l = d.split("\n")
arr = []
op = 0
op2 = 0
toCheck = []
pos = {}
for i in range(len(l)):
    if i == 0:
        arr = list(l[i].split(", "))
    if i >= 2:
        toCheck.append(l[i])
for i in range(len(arr)):
    pos[arr[i]] = 1

for i in range(len(toCheck)):

    temp = []
    full = ""
    seen = {}
    for j in range(len(toCheck[i])):
        full += toCheck[i][j]
        if full in pos:
            if len(full) not in seen:
                seen[len(full)] = 1
            else:
                seen[len(full)] += 1
        toAdd = {}
        for key, value in seen.items():
            if key >= len(full):
                continue
            if full[key:] in pos:
                if len(full) not in seen:
                    if len(full[key:])+(key) in toAdd:
                        toAdd[len(full[key:])+(key)] += value
                    else:
                        toAdd[len(full[key:])+(key)] = value
                else:
                    seen[len(full[key:])+(key)] += value
        for key, value in toAdd.items():
            seen[key] = value
    if len(toCheck[i]) in seen:
        op += 1
        op2 += seen[len(toCheck[i])]


print(op)
print(op2)
