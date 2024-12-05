import numpy as np

# Path to the input file
file_path = 'input1.txt'

# Character-to-integer mapping
char_to_int = {'M': 1, 'A': 2, 'S': 3, '.': 0}

# Define the X-MAS mask
xmas_mask = np.array([
    [1, 0, 3],  # M . S
    [0, 2, 0],  # . A .
    [1, 0, 3]   # M . S
])

# Read the grid from the input file and convert to numeric values
print(f"Reading the word search from: {file_path}")
with open(file_path, 'r') as file:
    grid = [list(line.strip()) for line in file]

# Convert the grid to a numeric matrix
grid_matrix = np.array([[char_to_int.get(char, 0) for char in row] for row in grid])

# Dimensions
rows, cols = grid_matrix.shape
mask_rows, mask_cols = xmas_mask.shape

# Count X-MAS patterns
count = 0

# Slide the 3x3 mask over the grid
for i in range(rows - mask_rows + 1):
    for j in range(cols - mask_cols + 1):
        # Extract the 3x3 window
        subgrid = grid_matrix[i:i + mask_rows, j:j + mask_cols]
        
        # Check if the subgrid matches the X-MAS mask
        if np.array_equal(subgrid * (xmas_mask > 0), xmas_mask):
            count += 1
            print(f"X-MAS found at center ({i+1}, {j+1})")

# Output the total count
print(f"\nTotal occurrences of X-MAS: {count}")
