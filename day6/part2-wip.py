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
    
    # Set to track visited positions with direction
    visited_positions = set()
    path = []
    turning_points = set()
    
    while True:
        # Track position with direction
        state = (guard_pos, guard_dir)
        if state in visited_positions:
            break  # Detected a loop
        
        visited_positions.add(state)
        path.append(state)
        
        # Calculate the position directly ahead
        dr, dc = direction_map[guard_dir]
        ahead_pos = (guard_pos[0] + dr, guard_pos[1] + dc)
        
        # Check if the guard is moving out of bounds
        if not (0 <= ahead_pos[0] < rows and 0 <= ahead_pos[1] < cols):
            break  # Guard leaves the map
        
        # Check for obstacle directly ahead
        if grid[ahead_pos[0]][ahead_pos[1]] == '#':
            # Record turning point
            turning_points.add(guard_pos)
            # Turn right
            guard_dir = right_turn[guard_dir]
        else:
            # Move forward
            guard_pos = ahead_pos
    
    return turning_points, path


def count_obstruction_points(grid):
    rows, cols = len(grid), len(grid[0])
    
    # Simulate the guard's original path to find turning points
    turning_points, _ = simulate_guard_path(grid)
    
    obstruction_points = set()
    
    # Test obstruction placement only around turning points
    for r, c in turning_points:  # Unpack the tuple directly
        for dr, dc in direction_map.values():
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '.':
                # Temporarily place an obstruction
                grid[nr][nc] = '#'
                _, path_with_obstruction = simulate_guard_path(grid)
                
                # Check if placing the obstruction creates a loop
                visited_states = set(path_with_obstruction)
                if len(visited_states) < len(path_with_obstruction):  # Loop detected
                    obstruction_points.add((nr, nc))
                
                # Remove the obstruction
                grid[nr][nc] = '.'
    
    return len(obstruction_points)


# Read the input map from the file
input_file = "input.txt"
with open(input_file, 'r') as file:
    grid = [list(line.strip()) for line in file]

# Count the possible obstruction points
result = count_obstruction_points(grid)
print(f"Number of positions to place an obstruction: {result}")
