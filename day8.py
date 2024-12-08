# really slow today but whatever. not a fan of this problem
import copy
import heapq
import math
import collections
import itertools
d = open("day8input.txt").read().strip()
l = d.split("\n")
locs = {}
marked = []
m1 = []
for i in range(len(l)):
    marked.append(["."]*len(l[i]))
    m1.append(["."]*len(l[i]))
op = 0
op2 = 0
for i in range(len(l)):
    for j in range(len(l[i])):
        if l[i][j] != ".":
            if l[i][j] not in locs:
                locs[l[i][j]] = [[i, j]]
            else:
                locs[l[i][j]].append([i, j])
for key, value in locs.items():
    for i in range(len(value)):
        for j in range(i+1, len(value)):
            first = value[i][0]-value[j][0]
            second = value[i][1]-value[j][1]
            t1 = value[i][0]+first
            t2 = value[i][1]+second
            t3 = value[j][0]-first
            t4 = value[j][1]-second
            while t1 >= 0 and t1 < len(l) and t2 >= 0 and t2 < len(l[0]):
                marked[t1][t2] = "X"
                t1 += first
                t2 += second
            while t3 >= 0 and t3 < len(l) and t4 >= 0 and t4 < len(l[0]):
                marked[t3][t4] = "X"
                t3 -= first
                t4 -= second
            if value[i][0]+first >= 0 and value[i][0]+first < len(l) and value[i][1]+second >= 0 and value[i][1]+second < len(l[0]):
                m1[value[i][0]+first][value[i][1]+second] = "X"
            if value[j][0]-first >= 0 and value[j][0]-first < len(l) and value[j][1]-second >= 0 and value[j][1]-second < len(l[0]):
                m1[value[j][0]-first][value[j][1]-second] = "X"
for i in range(len(l)):
    for j in range(len(l[i])):
        if l[i][j] != ".":
            marked[i][j] = "X"
for i in range(len(marked)):
    for j in range(len(marked[i])):
        if marked[i][j] == "X":
            op2 += 1
        if m1[i][j] == "X":
            op += 1
print(op)
print(op2)
