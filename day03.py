# Advent of Code 2025 - Day 3
# Solution 

def find_max_joltage(battery_bank, target_length):
    current_index = 0
    total_digits = len(battery_bank)
    result_digits = "" 

    for step in range(target_length):
        digits_needed_later = target_length - 1 - step
        search_limit = total_digits - digits_needed_later
        max_digit = -1
        max_digit_index = -1
        
        for i in range(current_index, search_limit):
            digit = int(battery_bank[i])
            if digit > max_digit:
                max_digit = digit
                max_digit_index = i
            if digit == 9:
                break
        
        result_string = str(max_digit)
        result_digits += result_string
        current_index = max_digit_index + 1
        
    return int(result_digits)

def main():
    with open('input.txt', 'r') as file:
        input_data = [line.strip() for line in file if line.strip()]

    # - PART 1 - 
    total_joltage_part1 = 0
    for bank in input_data:
        result = find_max_joltage(bank, target_length=2)
        total_joltage_part1 += result
    print(f"Part 1: {total_joltage_part1}")

    # - PART 2 - 
    total_joltage_part2 = 0
    for bank in input_data:
        result = find_max_joltage(bank, target_length=12)
        total_joltage_part2 += result
    print(f"Part 2: {total_joltage_part2}")

if __name__ == "__main__":
    main()