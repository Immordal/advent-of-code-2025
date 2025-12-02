# Advent of Code 2025 - Day 2
# Solution

with open('input.txt', 'r') as plik:
    content = plik.read().strip()

ranges = content.split(',')

# - PART 1 -
result1 = 0

for item in ranges:
    parts = item.split('-')
    start_num = int(parts[0])
    end_num = int(parts[1])
    
    for number in range(start_num, end_num + 1):
        text = str(number)
        length = len(text)
        
        if length % 2 == 0:
            half = length // 2
            left = text[:half]
            right = text[half:]
            
            if left == right:
                result1 = result1 + number

print("Answer 1:", result1)

# - PART 2 -
result2 = 0

for item in ranges:
    parts = item.split('-')
    start_num = int(parts[0])
    end_num = int(parts[1])
    
    for number in range(start_num, end_num + 1):
        text = str(number)
        length = len(text)
        found = False
        
        limit = (length // 2) + 1
        
        for pat_len in range(1, limit):
            if length % pat_len == 0:
                pattern = text[:pat_len]
                times = length // pat_len
                
                check = pattern * times
                
                if check == text:
                    found = True
                    break 
        
        if found == True:
            result2 = result2 + number

print("Answer 2:", result2)