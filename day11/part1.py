def has_even_digits(number):
    """Check if a number has an even number of digits."""
    return len(str(number)) % 2 == 0

def split_in_half(number):
    """Split a number with an even number of digits into two halves."""
    digits = str(number)
    mid = len(digits) // 2
    left = int(digits[:mid])
    right = int(digits[mid:])
    return [left, right]

def simulate_blinks(stones, num_blinks):
    """Simulate the transformation of stones over a given number of blinks."""
    for blink in range(num_blinks):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif has_even_digits(stone):
                new_stones.extend(split_in_half(stone))
            else:
                new_stones.append(stone * 2024)
        stones = new_stones
    return len(stones)

def main():
    # Read initial stones from the input file
    with open("input.txt", "r") as file:
        stones = list(map(int, file.read().strip().split()))
    
    num_blinks = 25
    result = simulate_blinks(stones, num_blinks)
    print(f"Number of stones after {num_blinks} blinks: {result}")

if __name__ == "__main__":
    main()
