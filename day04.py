# Advent of Code 2025 - Day 4
# Solution

# - PART 1 -

def solution1():
    diagram = []
    with open('input.txt', 'r') as file:
        for line in file:
            clean_line = line.strip()
            if len(clean_line) > 0:
                diagram.append(list(clean_line))

    total_rows = len(diagram)
    total_cols = len(diagram[0])
    ac_count = 0

    for row in range(total_rows):
        for col in range(total_cols):
            
            if diagram[row][col] != '@':
                continue

            directions = [
                (-1, -1), (-1, 0), (-1, 1),
                (0, -1),           (0, 1),
                (1, -1),  (1, 0),  (1, 1)
            ]
            
            nb_count = 0

            for move_r, move_c in directions:
                nb_row = row + move_r
                nb_col = col + move_c

                inside_rows = (0 <= nb_row < total_rows)
                inside_cols = (0 <= nb_col < total_cols)

                if inside_rows and inside_cols:
                    if diagram[nb_row][nb_col] == '@':
                        nb_count += 1
            
            if nb_count < 4:
                ac_count += 1

    print("Result part 1:", ac_count)

# - PART 2 -

def solution2():
    diagram = []
    with open('input.txt', 'r') as file:
        for line in file:
            clean_line = line.strip()
            if len(clean_line) > 0:
                diagram.append(list(clean_line))

    total_rows = len(diagram)
    total_cols = len(diagram[0])
    ac_counter = 0

    while True:
        to_remove = []
        
        for row in range(total_rows):
            for col in range(total_cols):
                
                if diagram[row][col] != '@':
                    continue

                directions = [
                    (-1, -1), (-1, 0), (-1, 1),
                    (0, -1),           (0, 1),
                    (1, -1),  (1, 0),  (1, 1)
                ]
                nb_count = 0

                for move_r, move_c in directions:
                    nb_row = row + move_r
                    nb_col = col + move_c
                    
                    inside_rows = (0 <= nb_row < total_rows)
                    inside_cols = (0 <= nb_col < total_cols)

                    if inside_rows and inside_cols:
                        if diagram[nb_row][nb_col] == '@':
                            nb_count += 1
                if nb_count < 4:
                    to_remove.append((row, col))

        counter = len(to_remove)

        if counter == 0:
            break

        ac_counter += counter

        for r, c in to_remove:
            diagram[r][c] = '.'

    print("Result part 2:", ac_counter)

if __name__ == "__main__":
    solution1()
    solution2()