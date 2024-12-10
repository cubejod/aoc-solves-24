import copy
import heapq
import math
from collections import Counter, deque
import itertools
d = open("day10input.txt").read().strip()
l = d.split("\n")
op = 0
op2 = 0
toCheck = deque()
for i in range(len(l)):
    for j in range(len(l[i])):
        if l[i][j] == "0":
            toCheck.append((i, j, 0))
while toCheck:
    cur = toCheck.popleft()
    if cur[2] == 9:
        op += 1
    else:
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for i in range(len(dirs)):
            ni = cur[0]+dirs[i][0]
            nj = cur[1]+dirs[i][1]

            if ni >= 0 and ni < len(l) and nj >= 0 and nj < len(l[0]):
                if l[ni][nj] != ".":
                    if int(l[ni][nj]) == cur[2]+1:
                        toCheck.append((ni, nj, cur[2]+1))


print(op)
print(op2)
