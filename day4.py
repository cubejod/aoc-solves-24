# more manual parsing... yuck!
import copy
import heapq
import math
import collections
d = open("day4input.txt").read().strip()
l = d.split("\n")
op = 0
op2 = 0
for i in range(len(l)):
    for j in range(len(l[i])):
        # up
        if i-3 >= 0:
            if l[i][j] == "X" and l[i-1][j] == "M" and l[i-2][j] == "A" and l[i-3][j] == "S":
                op += 1
        # down
        if i+3 < len(l):
            if l[i][j] == "X" and l[i+1][j] == "M" and l[i+2][j] == "A" and l[i+3][j] == "S":
                op += 1
        # left
        if j-3 >= 0:
            if l[i][j] == "X" and l[i][j-1] == "M" and l[i][j-2] == "A" and l[i][j-3] == "S":
                op += 1
        # right
        if j+3 < len(l[i]):
            if l[i][j] == "X" and l[i][j+1] == "M" and l[i][j+2] == "A" and l[i][j+3] == "S":
                op += 1
        # top left
        if i-3 >= 0 and j-3 >= 0:
            if l[i][j] == "X" and l[i-1][j-1] == "M" and l[i-2][j-2] == "A" and l[i-3][j-3] == "S":
                op += 1
        # top right
        if i-3 >= 0 and j+3 < len(l[i]):
            if l[i][j] == "X" and l[i-1][j+1] == "M" and l[i-2][j+2] == "A" and l[i-3][j+3] == "S":
                op += 1
        # bot left
        if i+3 < len(l) and j-3 >= 0:
            if l[i][j] == "X" and l[i+1][j-1] == "M" and l[i+2][j-2] == "A" and l[i+3][j-3] == "S":
                op += 1
        # bot right
        if i+3 < len(l) and j+3 < len(l[i]):
            if l[i][j] == "X" and l[i+1][j+1] == "M" and l[i+2][j+2] == "A" and l[i+3][j+3] == "S":
                op += 1
        # part 2 checks
        if i+2 < len(l) and j+2 < len(l[i]):
            if l[i][j] == "M" and l[i+1][j+1] == "A" and l[i+2][j+2] == "S" and l[i+2][j] == "M" and l[i+1][j+1] == "A" and l[i][j+2] == "S":
                op2 += 1
            if l[i][j] == "M" and l[i+1][j+1] == "A" and l[i+2][j+2] == "S" and l[i+2][j] == "S" and l[i+1][j+1] == "A" and l[i][j+2] == "M":
                op2 += 1
            if l[i][j] == "S" and l[i+1][j+1] == "A" and l[i+2][j+2] == "M" and l[i+2][j] == "M" and l[i+1][j+1] == "A" and l[i][j+2] == "S":
                op2 += 1
            if l[i][j] == "S" and l[i+1][j+1] == "A" and l[i+2][j+2] == "M" and l[i+2][j] == "S" and l[i+1][j+1] == "A" and l[i][j+2] == "M":
                op2 += 1
print(op)
print(op2)
