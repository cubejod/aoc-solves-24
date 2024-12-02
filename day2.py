# part 2 is O(n^2) and is really awful code!!!!! but i did write it pretty fast so...
import copy
d = open("day2input.txt").read().strip()
l = d.split("\n")
op = 0
op2 = 0


def check(nums):
    inc = True
    dec = True
    adj = True
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            dec = False
        if nums[i] < nums[i-1]:
            inc = False
    for i in range(1, len(nums)-1):
        if abs(nums[i]-nums[i-1]) > 3 or abs(nums[i]-nums[i-1]) < 1:
            adj = False
    if abs(nums[0]-nums[1]) > 3 or abs(nums[0]-nums[1]) < 1:
        adj = False
    if abs(nums[-1]-nums[-2]) > 3 or abs(nums[-1]-nums[-2]) < 1:
        adj = False
    if (inc or dec) and adj:
        return 1
    else:
        return 0


for line in l:
    nums = list(map(int, line.split()))
    if check(nums):
        op += 1
        op2 += 1
    else:
        for i in range(len(nums)):
            c = copy.deepcopy(nums)
            c.pop(i)
            if check(c):
                op2 += 1
                break

print(op)
print(op2)
