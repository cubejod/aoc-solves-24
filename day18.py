import copy
import heapq
import math
from collections import Counter, deque
import itertools
import re


def dijkstra(grid, s, e):
    rows, cols = len(grid), len(grid[0])
    # Up, Down, Left, Right. modify directions here!
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    pq = [(0, s)]  # (distance, (row, col))
    visited = set()
    while pq:
        dist, (x, y) = heapq.heappop(pq)
        if (x, y) == e:
            return dist
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != "#" and (nx, ny) not in visited:
                heapq.heappush(pq, (dist + 1, (nx, ny)))
    return -1


op = 0
op2 = 0
d = open("day18input.txt").read().strip()
l = d.split("\n")
grid = []
for i in range(71):
    grid.append(["."] * 71)
for i in range(len(l)):
    a, b = l[i].split(",")
    a = int(a)
    b = int(b)
    grid[b][a] = "#"
    if i >= 1024:
        s = (0, 0)
        e = (70, 70)
        best = dijkstra(grid, s, e)
        if i == 1024:
            op = best
        if best == -1:
            op2 = (f"{a},{b}")
            break
print(op)
print(op2)
