# itertools my beloved. sadly this brute force takes ~19 seconds to run
import copy
import heapq
import math
import collections
import itertools
import time
t = time.time()
d = open("day7input.txt").read().strip()
l = d.split("\n")
op = 0
op2 = 0
for line in l:
    left, right = line.split(":")
    left = int(left)
    nums = list(map(int, right.split()))
    operators = ["+", "x"]
    ope2 = ["+", "x", "||"]
    combos = itertools.product(operators, repeat=len(nums) - 1)
    for combo in combos:
        result = nums[0]
        for i, operator in enumerate(combo):
            if operator == "+":
                result += nums[i + 1]
            elif operator == "x":
                result *= nums[i + 1]
            if result > left:
                break
        if result == left:
            op += left
            break
    c2 = itertools.product(ope2, repeat=len(nums)-1)
    for c in c2:
        result = nums[0]
        for i, operator in enumerate(c):
            if operator == "+":
                result += nums[i + 1]
            elif operator == "x":
                result *= nums[i + 1]
            elif operator == "||":
                result = int(str(result)+str(nums[i+1]))
            if result > left:
                break
        if result == left:
            op2 += left
            break
    pass


print(op)
print(op2)
print(time.time()-t)
