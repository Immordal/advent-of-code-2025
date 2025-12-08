# Advent of Code 2025 - Day 8
# Solution

import math
from collections import Counter

# - PART 1 -

boxes = []
with open('input.txt', 'r') as f:
    for line in f:
        if line.strip():
            boxes.append(list(map(int, line.split(','))))

n = len(boxes)
cables = []
for i in range(n):
    for j in range(i + 1, n):
        dist = sum((boxes[i][k] - boxes[j][k])**2 for k in range(3))
        cables.append((dist, i, j))

cables.sort(key=lambda x: x[0])

links = list(range(n))
def find(i):
    if links[i] != i:
        links[i] = find(links[i])
    return links[i]

for _, u, v in cables[:1000]:
    links[find(u)] = find(v)

sizes = sorted(Counter(find(i) for i in range(n)).values(), reverse=True)
print("Solution for part1:",math.prod(sizes[:3]))

# - PART 2 -

boxes = []
with open('input.txt', 'r') as f:
    for line in f:
        if line.strip():
            boxes.append(list(map(int, line.split(','))))

n = len(boxes)
cables = []
for i in range(n):
    for j in range(i + 1, n):
        dist = sum((boxes[i][k] - boxes[j][k])**2 for k in range(3))
        cables.append((dist, i, j))

cables.sort(key=lambda x: x[0])

links = list(range(n))
count = n

for _, u, v in cables:
    root_u = find(u)
    root_v = find(v)
    if root_u != root_v:
        links[root_u] = root_v
        count -= 1
        if count == 1:
            print("Solution for part2:",boxes[u][0] * boxes[v][0])
            break