# Advent of Code 2025 - Day 9
# Solution

# - PART 1 -

red_tiles = []
with open('input.txt', 'r') as f:
    for line in f:
        if line.strip():
            red_tiles.append(list(map(int, line.strip().split(','))))

num_tiles = len(red_tiles)
max_area = 0

for i in range(num_tiles):
    for j in range(i + 1, num_tiles):
        t1 = red_tiles[i]
        t2 = red_tiles[j]
        
        width = abs(t1[0] - t2[0]) + 1
        height = abs(t1[1] - t2[1]) + 1
        area = width * height
        
        if area > max_area:
            max_area = area

print(max_area)

# - PART 2 -

red_tiles = []
with open('input.txt', 'r') as f:
    for line in f:
        if line.strip():
            red_tiles.append(list(map(int, line.strip().split(','))))

num_tiles = len(red_tiles)
walls = []

for i in range(num_tiles):
    p1 = red_tiles[i]
    p2 = red_tiles[(i + 1) % num_tiles]
    walls.append((min(p1[0], p2[0]), min(p1[1], p2[1]), max(p1[0], p2[0]), max(p1[1], p2[1])))

max_area = 0

for i in range(num_tiles):
    for j in range(i + 1, num_tiles):
        p1 = red_tiles[i]
        p2 = red_tiles[j]
        
        rx1, rx2 = min(p1[0], p2[0]), max(p1[0], p2[0])
        ry1, ry2 = min(p1[1], p2[1]), max(p1[1], p2[1])
        
        area = (rx2 - rx1 + 1) * (ry2 - ry1 + 1)
        
        if area <= max_area:
            continue

        mid_x = (rx1 + rx2) / 2
        mid_y = (ry1 + ry2) / 2
        
        walls_crossed = 0
        for wx1, wy1, wx2, wy2 in walls:
            if wx1 == wx2 and wx1 > mid_x:
                if wy1 <= mid_y < wy2:
                    walls_crossed += 1
        
        if walls_crossed % 2 == 0:
            continue

        collision = False
        for wx1, wy1, wx2, wy2 in walls:
            if wy1 == wy2:
                if ry1 < wy1 < ry2:
                    if not (wx2 <= rx1 or wx1 >= rx2):
                        collision = True
                        break
            else:
                if rx1 < wx1 < rx2:
                    if not (wy2 <= ry1 or wy1 >= ry2):
                        collision = True
                        break
        
        if not collision:
            max_area = area

print(max_area)