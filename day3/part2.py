import re

# Path to the input file
file_path = 'input1.txt'

# Regular expressions for instructions
mul_pattern = re.compile(r'mul\(\s*(\d+)\s*,\s*(\d+)\s*\)')
do_pattern = re.compile(r'do\(\)')
dont_pattern = re.compile(r"don't\(\)")

# Read the corrupted memory from the file
print(f"Reading the corrupted memory from: {file_path}")
with open(file_path, 'r') as file:
    corrupted_memory = file.read()

# Initialize state and total sum
mul_enabled = True  # Initially, mul instructions are enabled
total_sum = 0

# Process the memory linearly
for match in re.finditer(r"mul\(\s*\d+\s*,\s*\d+\s*\)|do\(\)|don't\(\)", corrupted_memory):
    instruction = match.group()

    # Handle do() and don't() instructions
    if do_pattern.fullmatch(instruction):
        mul_enabled = True
        print("do() encountered: mul instructions enabled.")
    elif dont_pattern.fullmatch(instruction):
        mul_enabled = False
        print("don't() encountered: mul instructions disabled.")

    # Handle mul(X, Y) instructions
    elif mul_enabled and mul_pattern.fullmatch(instruction):
        x, y = map(int, mul_pattern.match(instruction).groups())
        product = x * y
        total_sum += product
        print(f"mul({x}, {y}) -> {product} (included in sum)")

    # Invalid mul instruction or mul disabled
    else:
        print(f"{instruction} -> mul instructions disabled or invalid (ignored).")

# Final result
print(f"\nTotal sum of all enabled mul() results: {total_sum}")
