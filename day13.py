# super cancer p2. probably should have just done old fasioned math but i tried numpy and had precision issues so i had to switch to sympy
import copy
from sympy import Matrix
import heapq
import math
from collections import Counter, deque
import itertools
d = open("day13input.txt").read().strip()
l = d.split("\n")

op = 0
op2 = 0
vals = []
for i in range(len(l)):
    if i % 4 == 0:
        vals.append([])
        a = list(l[i].split())
        vals[-1].append(int(a[2][2:4]))
        vals[-1].append(int(a[3][2:4]))
    elif i % 4 == 1:
        a = list(l[i].split())
        vals[-1].append(int(a[2][2:4]))
        vals[-1].append(int(a[3][2:4]))
    elif i % 4 == 2:
        a = list(l[i].split())
        vals[-1].append(int(a[1][2:-1]))
        vals[-1].append(int(a[2][2:]))
for i in range(len(vals)):
    m1 = Matrix([[vals[i][0], vals[i][2]],
                [vals[i][1], vals[i][3]]])
    m2 = Matrix([vals[i][4]+10000000000000, vals[i][5]+10000000000000])
    ans = m1.solve(m2)
    c1, c2 = ans[0], ans[1]
    if c1 == int(c1) and c2 == int(c2):
        op2 += (c1*3)+c2
    m2 = Matrix([vals[i][4], vals[i][5]])
    ans = m1.solve(m2)
    c1, c2 = ans[0], ans[1]
    if c1 == int(c1) and c2 == int(c2):
        op += (c1*3)+c2


print(op)
print(op2)
