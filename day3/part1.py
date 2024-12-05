import re

# Path to the input file
file_path = 'input1.txt'

# Regular expression to match valid mul(X, Y) instructions
mul_pattern = re.compile(r'mul\(\s*(\d+)\s*,\s*(\d+)\s*\)')

# Read the corrupted memory from the file
print(f"Reading the corrupted memory from: {file_path}")
with open(file_path, 'r') as file:
    corrupted_memory = file.read()

# Find all valid mul(X, Y) instructions
matches = mul_pattern.findall(corrupted_memory)

# Compute the sum of all products
total_sum = 0
for match in matches:
    x, y = map(int, match)  # Convert the matched strings to integers
    product = x * y
    total_sum += product
    print(f"Found mul({x}, {y}) -> {product}")

# Output the total sum
print(f"\nTotal sum of all valid mul() results: {total_sum}")
