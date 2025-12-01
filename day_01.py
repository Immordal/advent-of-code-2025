# Advent of Code 2025 - Day 1
# Solution

with open('input.txt', 'r') as plik:
    lines = plik.readlines()

# - PART 1 -
position = 50
result1 = 0

for line in lines:
    line = line.strip() 
    if not line:
        continue 
    
    direction = line[0]       
    number = int(line[1:])   
    
    if direction == 'L':
        position = position - number
    else:
        position = position + number
        
    position = position % 100
    
    if position == 0:
        result1 = result1 + 1

print("Answer 1:", result1)

# - PART 2 -
position = 50  
result2 = 0

for line in lines:
    line = line.strip()
    if not line:
        continue

    direction = line[0]
    number = int(line[1:])
    
    old_pos = position 
    
    if direction == 'R':
        position = position + number
        
        count = (position // 100) - (old_pos // 100)
        result2 = result2 + count
    else: 
        position = position - number
        
        count = ((old_pos - 1) // 100) - ((position - 1) // 100)
        result2 = result2 + count

print("Answer 2:", result2)