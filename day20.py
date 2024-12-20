import copy
import heapq
import math
from collections import Counter, deque
import itertools
import re

d = open("day20input.txt").read().strip()
l = d.split("\n")
op = 0
op2 = 0
path = []
for i in range(len(l)):
    for j in range(len(l[i])):
        if l[i][j] == "S":
            s = (i, j)
        elif l[i][j] == "E":
            e = (i, j)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
seen = set()
vals = {}
cost = 0
least = 99999999999
while s != e:
    temp = []
    tt = []
    ttSeen = set()
    ns = s
    path.append(s)
    for i in range(len(directions)):
        nx = s[0]+directions[i][0]
        ny = s[1]+directions[i][1]
        if nx >= 0 and nx < len(l) and ny >= 0 and ny < len(l[0]):
            if l[nx][ny] == "E":
                ns = (nx, ny)
                path.append(ns)
                break
            if l[nx][ny] == "." and (nx, ny) not in seen:
                ns = (nx, ny)
                seen.add((nx, ny))
    s = ns
for i in range(len(path)):
    for j in range(i+100, len(path)):
        dist = abs(path[j][0]-path[i][0])+abs(path[j][1]-path[i][1])
        if j - i - dist < 100:
            continue
        if dist == 2:
            op += 1
        if dist <= 20:
            op2 += 1
print(op)
print(op2)
