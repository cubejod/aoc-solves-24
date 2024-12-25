# slow and messy, classic.
import copy
import heapq
import math
from collections import Counter, deque
import itertools
import re
d = open("day25input.txt").read().strip()
l = d.split("\n")
temp = []
arr = []
op = 0
op2 = 0
for line in l:
    if len(line) > 1:
        temp.append(line)
    else:
        arr.append(temp)
        temp = []
if temp != []:
    arr.append(temp)
lock = []
key = []
for i in range(len(arr)):
    if arr[i][0] == "#####":
        lock.append(arr[i])
    else:
        key.append(arr[i])
l2 = []
k2 = []
for i in range(len(lock)):
    t = []
    cur = lock[i]
    for j in range(len(cur[0])):
        for k in range(len(cur)):
            if cur[k][j] == ".":
                t.append(k-1)
                break
    l2.append(t)
for i in range(len(key)):
    cur = key[i]
    t = []
    for j in range(len(cur[0])):
        for k in range(len(cur)-1, -1, -1):
            if cur[k][j] == ".":
                t.append(len(cur)-k-2)
                break
    k2.append(t)

found = set()
for i in range(len(l2)):
    for j in range(len(k2)):
        flag = True
        for k in range(len(l2[0])):
            if l2[i][k]+k2[j][k] >= 6:
                flag = False
                break
        if flag:
            temp = tuple(l2[i]+k2[j])
            if temp not in found:
                op += 1
                found.add(temp)
op2 = "just click the button lol"
print(op)
print(op2)
