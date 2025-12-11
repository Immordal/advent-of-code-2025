# Advent of Code 2025 - Day 10
# Solution 
import re
from itertools import combinations

# - PART 1 -

total = 0
with open('input.txt', 'r') as file:
    lines = file.read().strip().split('\n')

for line in lines:
    raw_target = re.search(r'\[(.*?)\]', line).group(1)
    target_list = [1 if char == '#' else 0 for char in raw_target]

    buttons_list = []
    for m in re.findall(r'\(([\d,]+)\)', line):
        indexes = [int(x) for x in m.split(',')]
        buttons_list.append(indexes)

    raw_values = re.search(r'\{([\d,]+)\}', line).group(1)
    values_list = [int(x) for x in raw_values.split(',')]

    found_solution = False
    
    for k in range(len(buttons_list) + 1):
        for combo in combinations(buttons_list, k):
            current_state = [0] * len(target_list)
   
            for btn_indexes in combo:
                for idx in btn_indexes:
                    current_state[idx] = 1 - current_state[idx]
            
            if current_state == target_list:
                total += k
                found_solution = True
                break
        
        if found_solution:
            break


print("Answer for part 1:" , total)

