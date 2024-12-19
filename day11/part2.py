def has_even_digits(number):
    """Check if a number has an even number of digits."""
    return len(str(number)) % 2 == 0

def split_in_half(number):
    """Split a number with an even number of digits into two halves."""
    digits = str(number)
    mid = len(digits) // 2
    left = int(digits[:mid])
    right = int(digits[mid:])
    return left, right

def increment_count(freq_dict, stone, count):
    """Increment the count of a stone in the frequency dictionary."""
    if stone in freq_dict:
        freq_dict[stone] += count
    else:
        freq_dict[stone] = count

def simulate_optimized_blinks(stones, num_blinks):
    """Simulate the transformation of stones over a given number of blinks."""
    # Initialize frequency dictionary
    freq = {}
    for stone in stones:
        increment_count(freq, stone, 1)
    
    # Perform transformations for each blink
    for blink in range(num_blinks):
        next_freq = {}
        for stone, count in freq.items():
            if stone == 0:
                increment_count(next_freq, 1, count)
            elif has_even_digits(stone):
                left, right = split_in_half(stone)
                increment_count(next_freq, left, count)
                increment_count(next_freq, right, count)
            else:
                new_stone = stone * 2024
                increment_count(next_freq, new_stone, count)
        freq = next_freq
    
    # Total number of stones
    return sum(freq.values())

def main():
    # Read initial stones from the input file
    with open("input.txt", "r") as file:
        stones = list(map(int, file.read().strip().split()))
    
    num_blinks = 75
    result = simulate_optimized_blinks(stones, num_blinks)
    print(f"Number of stones after {num_blinks} blinks: {result}")

if __name__ == "__main__":
    main()
