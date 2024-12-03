# i wrote the worst input parsing ever and was asked to leave the computer
import copy
import heapq
import math
import collections
d = open("day3input.txt").read().strip()
l = d.split("\n")
op = 0
op2 = 0
nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
valid = []
v2 = []
enabled = True
for line in l:
    cur = ""
    needed = "m"
    for i in range(len(line)):
        if i > 7:
            if line[i-7:i] == "don't()":
                enabled = False
            if line[i-4:i] == "do()":
                enabled = True
        if needed == "m" and line[i] == "m":
            cur += "m"
            needed = "u"
        elif needed == "u" and line[i] == "u":
            cur += "u"
            needed = "l"
        elif needed == "l" and line[i] == "l":
            cur += "l"
            needed = "("
        elif needed == "(" and line[i] == "(":
            cur += "("
            needed = ","
        elif needed == "," and line[i] in nums:
            cur += line[i]
        elif needed == "," and line[i] == ",":
            cur += ","
            needed = ")"
        elif needed == ")" and line[i] in nums:
            cur += line[i]
        elif needed == ")" and line[i] == ")":
            cur += ")"
            needed = "m"
            valid.append(cur)
            if enabled:
                v2.append(cur)
            cur = ""
        else:
            cur = ""
            needed = "m"

    pass

for i in range(len(valid)):
    valid[i] = valid[i][4:-1]
    a, b = valid[i].split(",")
    a, b = int(a), int(b)
    op += a*b
for i in range(len(v2)):
    v2[i] = v2[i][4:-1]
    a, b = v2[i].split(",")
    a, b = int(a), int(b)
    op2 += a*b
print(op)
print(op2)
