# Advent of Code 2025 - Day 6
# Solution 
import math

# - PART1 -

with open('input.txt', 'r') as file:
    lines = [line.strip().split() for line in file]
    columns = list(zip(*lines))
solution = 0

for *nums, op in columns:
    numbers = [int(n) for n in nums]
    result = 0
    if op == '+':
        result = sum(numbers)
    elif op == '*':
        result = math.prod(numbers)

    solution += result        

print("Solution for Part1:",solution)  

# - PART2 -

with open('input.txt', 'r') as file:
    grid = [line.strip("\n") for line in file]
    columns = list(zip(*grid))


groups = []
c_group = []

for column in columns:
    if set(column) == {" "}:
        groups.append(c_group)
        c_group = []
    else:
        c_group.append(column)

groups.append(c_group)
solution2 = 0
for group in groups:
    numbers = [int("".join(col[:-1])) for col in group]
  
    operator = group[0][-1]
    if operator == '+':
        solution2 += sum(numbers)
    elif operator == '*':
        solution2 += math.prod(numbers) 

print("Solution for Part2:",solution2)