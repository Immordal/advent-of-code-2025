# Advent of Code 2025 - Day 7
# Solution
from collections import defaultdict

# - PART 1 -

with open('input.txt', 'r') as file:
        grid = [list(line.strip()) for line in file]

height = len(grid)
width = len(grid[0])
total = 0

for r in range(height):
    for c in range(width):
                if ((grid[r-1][c] == '|' or grid[r-1][c] == 'S') and grid[r][c] == '.'):
                    grid[r][c] = '|' 

                if grid[r][c] == '^':
                    if c - 1 >= 0 and grid[r][c-1] == '.':
                        grid[r][c-1] = '|'
                    if c + 1 < width and grid[r][c+1] == '.':
                        grid[r][c+1] = '|'
for r in range(height):
    for c in range(width):
          if ((grid[r-1][c] == '|' or grid[r-1][c] == 'S') and grid[r][c] == '^'):
                total += 1

print("solution for part1:", total)

# - PART 2 -

with open('input.txt', 'r') as f:
        grid = [line.strip() for line in f]

height = len(grid)
width = len(grid[0])
timelines = defaultdict(int)
start_row = 0

for r in range(height):
        for c in range(width):
            if grid[r][c] == 'S':
                timelines[c] = 1  
                start_row = r
                break
    
for r in range(start_row + 1, height):
        next_timelines = defaultdict(int) 
        for col, count in timelines.items():
            char = grid[r][col]
            
            if char == '^':
                if col - 1 >= 0:
                    next_timelines[col - 1] += count
                if col + 1 < width:
                    next_timelines[col + 1] += count
                    
            else:
                next_timelines[col] += count
        timelines = next_timelines
        if not timelines:
            break
result = sum(timelines.values())
print("Solution for part2:", result)



