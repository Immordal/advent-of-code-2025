# Advent of Code 2025 - Day 5
# Solution

with open('input.txt', 'r') as file:
    text = file.read().strip()

parts = text.split('\n\n')

ranges_part = parts[0]  
numbers_part = parts[1] 

list_ranges = []
lines = ranges_part.split('\n')
for line in lines:
    split_line = line.split('-')
    start = int(split_line[0])
    end = int(split_line[1])
    list_ranges.append((start, end))

list_numbers = []
lines = numbers_part.split('\n')
for line in lines:
    list_numbers.append(int(line))

# - PART 1 -

result1 = 0

for candidate in list_numbers:
    is_fresh = False
    for start, end in list_ranges:
        if candidate >= start and candidate <= end:
            is_fresh = True
            break 
            
    if is_fresh == True:
        result1 = result1 + 1

print("Answer 1:", result1)

# - PART 2 - 

list_ranges.sort()

merged_ranges = []

if len(list_ranges) > 0:
    current_start = list_ranges[0][0]
    current_end = list_ranges[0][1]

    for i in range(1, len(list_ranges)):
        next_start = list_ranges[i][0]
        next_end = list_ranges[i][1]

        if next_start <= current_end + 1:
            if next_end > current_end:
                current_end = next_end
        else:
          
            merged_ranges.append((current_start, current_end))
            current_start = next_start
            current_end = next_end

    merged_ranges.append((current_start, current_end))

result2 = 0

for start, end in merged_ranges:
    length = end - start + 1
    result2 = result2 + length

print("Answer 2:", result2)