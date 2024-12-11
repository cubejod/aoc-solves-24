# tried to do a mathy solve for part 2 before realizing i could just cache stuff... not that the math solve is impossible, it's actually quite easy, i just suck.
import copy
import heapq
import math
from collections import Counter, deque
import itertools
from functools import cache
d = open("day11input.txt").read().strip()
l = list(map(int, d.split()))
op = 0
op2 = 0


@cache
def process(num, blinks):
    if blinks == 0:
        return 1
    if num == 0:
        return process(1, blinks-1)
    elif len(str(num)) % 2 == 0:
        cur = str(num)
        left = cur[0:len(cur)//2]
        right = cur[(len(cur)//2):]
        return process(int(left), blinks-1) + process(int(right), blinks-1)
    else:
        return process(num*2024, blinks-1)


for i in range(len(l)):
    op += process(l[i], 25)
    op2 += process(l[i], 75)
print(op)
print(op2)
