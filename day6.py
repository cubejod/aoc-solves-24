# really slow and sloppy today. original code took 8.5 minutes to run, this is 100x faster with some optimizations. includes timer for reference!
import copy
import heapq
import math
import collections
import time
time1 = time.time()
d = open("day6input.txt").read().strip()
l = d.split("\n")
for i in range(len(l)):
    l[i] = list(l[i])
op = 0
op2 = 0
iPos = 0
jPos = 0
dir = "up"
arr = []
arr2 = []
for i in range(len(l)):
    arr.append(["."]*len(l[i]))
    arr2.append(["."]*len(l[i]))
    for j in range(len(l[i])):
        if l[i][j] == "^":
            iPos = i
            jPos = j
            break
op += 1
f = True
i = iPos
j = jPos


def simulate(i, j, dir, ci, cj):
    l[ci][cj] = "#"
    seen = set()
    while True:
        if (i, j, dir) in seen:
            l[ci][cj] = "."
            return 1
        seen.add((i, j, dir))
        if dir == "up":
            if i == 0:
                break
            if l[i-1][j] == "#":
                dir = "right"
            else:
                i -= 1

        elif dir == "down":
            if i == len(l)-1:
                break
            if l[i+1][j] == "#":
                dir = "left"
            else:
                i += 1

        elif dir == "left":
            if j == 0:
                break
            if l[i][j-1] == "#":
                dir = "up"
            else:
                j -= 1

        elif dir == "right":
            if j == len(l[i])-1:
                break
            if l[i][j+1] == "#":
                dir = "down"
            else:
                j += 1
    l[ci][cj] = "."
    return 0


first = True
last = "down"
while True:
    if first:
        first = False
    else:
        if simulate(iPos, jPos, "up", i, j):
            arr2[i][j] = "X"
    if dir == "up":
        if i == 0:
            break
        if l[i-1][j] == "#":
            dir = "right"
        else:
            i -= 1
            arr[i][j] = "X"

    elif dir == "down":
        if i == len(l)-1:
            break
        if l[i+1][j] == "#":
            dir = "left"
        else:
            i += 1
            arr[i][j] = "X"

    elif dir == "left":
        if j == 0:
            break
        if l[i][j-1] == "#":
            dir = "up"
        else:
            j -= 1
            arr[i][j] = "X"

    elif dir == "right":
        if j == len(l[i])-1:
            break
        if l[i][j+1] == "#":
            dir = "down"
        else:
            j += 1
            arr[i][j] = "X"

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == "X":
            op += 1
        if arr2[i][j] == "X":
            op2 += 1
print(op)
print(op2)
print(time.time()-time1)
