# Define the map and movement rules
direction_map = {
    '^': (-1, 0),  # Up
    '>': (0, 1),   # Right
    'v': (1, 0),   # Down
    '<': (0, -1)   # Left
}

# Right turn: maps current direction to the new direction after a right turn
right_turn = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^'
}

def simulate_guard_path(grid):
    rows, cols = len(grid), len(grid[0])
    
    # Find the initial position and direction of the guard
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in '^>v<':
                guard_pos = (r, c)
                guard_dir = grid[r][c]
                break
    
    # Set to track visited positions
    visited_positions = set()
    visited_positions.add(guard_pos)
    
    # Simulate the guard's movement
    while True:
        # Calculate the position directly ahead
        dr, dc = direction_map[guard_dir]
        ahead_pos = (guard_pos[0] + dr, guard_pos[1] + dc)
        
        # Check if the guard is moving out of bounds
        if not (0 <= ahead_pos[0] < rows and 0 <= ahead_pos[1] < cols):
            break  # Guard leaves the map
        
        # Check for obstacle directly ahead
        if grid[ahead_pos[0]][ahead_pos[1]] == '#':
            # Turn right
            guard_dir = right_turn[guard_dir]
        else:
            # Move forward
            guard_pos = ahead_pos
            visited_positions.add(guard_pos)
    
    return len(visited_positions)

# Read the input map from the file
input_file = "input.txt"
with open(input_file, 'r') as file:
    grid = [list(line.strip()) for line in file]

# Simulate the guard's movement and get the result
result = simulate_guard_path(grid)
print(f"Total distinct positions visited by the guard: {result}")
