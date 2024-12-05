# no topo sort because im LAZY and don't have an implementation of it ready to copy paste. lost 15 min on p2 to bugs because this code is awful
import copy
import heapq
import math
import collections
d = open("day5input.txt").read().strip()
l = d.split("\n")
op = 0
op2 = 0
flag = False
rules = {}
arr = []
for line in l:
    if flag == False:
        if line == "":
            flag = True
            continue
        a, b = map(int, line.split("|"))
        if a in rules:
            rules[a].append(b)
        else:
            rules[a] = [b]
    else:
        nums = list(map(int, line.split(",")))
        arr.append(nums)
    pass
good = []
bad = []
for i in range(len(arr)):
    seen = {}
    f = True
    for j in range(len(arr[i])):
        if arr[i][j] in rules:
            for k in range(len(rules[arr[i][j]])):
                if rules[arr[i][j]][k] in seen:
                    f = False
                    break
        seen[arr[i][j]] = 1
    if f:
        good.append(arr[i])
    else:
        bad.append(arr[i])
for i in range(len(good)):
    op += good[i][len(good[i])//2]
for i in range(len(bad)):
    while True:
        seen = {}
        f = True
        for j in range(len(bad[i])):
            if bad[i][j] in rules:
                for k in range(len(rules[bad[i][j]])):
                    if rules[bad[i][j]][k] in seen:
                        f = False
                        temp = bad[i][j]
                        bad[i].pop(j)
                        bad[i].insert(j-1, temp)
                        break
            seen[bad[i][j]] = 1
        if f:
            break
for i in range(len(bad)):
    op2 += bad[i][len(bad[i])//2]
print(op)
print(op2)
