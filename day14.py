# lame p2. threw a guess at the wall and it stuck, not sure how anybody was supposed to figure it out from the problem description...
import os
import copy
import heapq
import math
from collections import Counter, deque
import itertools
d = open("day14input.txt").read().strip()
l = d.split("\n")
op = 0
op2 = 0
width = 101
height = 103
arr = []
for i in range(len(l)):
    a, b = l[i].split()
    t1, t2 = a.split(",")
    t1 = t1[2:]
    t3, t4 = b.split(",")
    t3 = t3[2:]
    t1, t2, t3, t4 = int(t1), int(t2), int(t3), int(t4)
    arr.append([t1, t2, t3, t4])
iteration = 0
while True:
    iteration += 1
    if iteration == 101:
        q1, q2, q3, q4 = 0, 0, 0, 0
        for i in range(len(arr)):
            if arr[i][0] <= 49 and arr[i][1] <= 50:
                q1 += 1
            elif arr[i][0] <= 49 and arr[i][1] >= 52:
                q2 += 1
            elif arr[i][0] >= 51 and arr[i][1] <= 50:
                q3 += 1
            elif arr[i][0] >= 51 and arr[i][1] >= 52:
                q4 += 1
        op = q1*q2*q3*q4
    for i in range(len(arr)):
        arr[i][0] += arr[i][2]
        arr[i][1] += arr[i][3]
        arr[i][0] %= width
        arr[i][1] %= height
    temp = []
    for i in range(height):
        temp.append(["_"] * width)
    flag = True
    for i in range(len(arr)):
        if temp[arr[i][1]][arr[i][0]] == "O":
            flag = False
            break
        temp[arr[i][1]][arr[i][0]] = "O"
    if flag:
        op2 = iteration
        break
print(op)
print(op2)
