# Path to the input file
file_path = 'input1.txt'

# The word to search for
target_word = "XMAS"

# Directions: (dx, dy) for all 8 directions (horizontal, vertical, diagonal)
directions = [
    (0, 1),   # Right
    (0, -1),  # Left
    (1, 0),   # Down
    (-1, 0),  # Up
    (1, 1),   # Down-Right
    (1, -1),  # Down-Left
    (-1, 1),  # Up-Right
    (-1, -1)  # Up-Left
]

# Read the grid from the input file
print(f"Reading the word search from: {file_path}")
with open(file_path, 'r') as file:
    grid = [list(line.strip()) for line in file]

rows = len(grid)
cols = len(grid[0])
word_length = len(target_word)
count = 0

# Function to check if the word exists starting from (x, y) in direction (dx, dy)
def is_word_at(x, y, dx, dy):
    for i in range(word_length):
        nx, ny = x + i * dx, y + i * dy
        if not (0 <= nx < rows and 0 <= ny < cols):  # Out of bounds
            return False
        if grid[nx][ny] != target_word[i]:  # Character mismatch
            return False
    return True

# Search for the word in all directions
for x in range(rows):
    for y in range(cols):
        for dx, dy in directions:
            if is_word_at(x, y, dx, dy):
                count += 1
                print(f"Found '{target_word}' at ({x}, {y}) in direction ({dx}, {dy})")

# Output the total count
print(f"\nTotal occurrences of '{target_word}': {count}")
