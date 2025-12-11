# Advent of Code 2025 - Day 11
# Solution

# - PART 1 -

devices = {}
for line in open("input.txt"):
    if line.strip():
        name, outputs = line.split(":")
        devices[name.strip()] = outputs.strip().split()

memo = {}
def count_paths(current, target):
    if current == target: return 1
    if current not in devices: return 0
    if (current, target) in memo: return memo[(current, target)]
    
    total = sum(count_paths(output, target) for output in devices[current])
    memo[(current, target)] = total
    return total

print(count_paths('you', 'out'))

# - PART 2 -

devices = {}
for line in open("input.txt"):
    if line.strip():
        name, outputs = line.split(":")
        devices[name.strip()] = outputs.strip().split()

memo = {}
path1 = count_paths('svr', 'dac') * count_paths('dac', 'fft') * count_paths('fft', 'out')
path2 = count_paths('svr', 'fft') * count_paths('fft', 'dac') * count_paths('dac', 'out')

print(path1 + path2)