def parse_map(file_path):
    """Reads the input file and parses the map into a grid."""
    with open(file_path, 'r') as file:
        return [list(map(int, line.strip())) for line in file]

def find_neighbors(grid, x, y):
    """Returns valid neighbors (up, down, left, right) of a cell."""
    neighbors = []
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            neighbors.append((nx, ny))
    return neighbors

def find_distinct_trails(grid, start_x, start_y):
    """Find all distinct hiking trails starting from a given trailhead."""
    rows, cols = len(grid), len(grid[0])
    visited_trails = set()
    stack = [(start_x, start_y, [(start_x, start_y)])]  # (x, y, path)

    while stack:
        x, y, path = stack.pop()

        if grid[x][y] == 9:
            visited_trails.add(tuple(path))
            continue

        for nx, ny in find_neighbors(grid, x, y):
            if grid[nx][ny] == grid[x][y] + 1 and (nx, ny) not in path:
                stack.append((nx, ny, path + [(nx, ny)]))

    return len(visited_trails)

def calculate_total_rating(grid):
    """Calculate the sum of ratings of all trailheads."""
    total_rating = 0
    rows, cols = len(grid), len(grid[0])

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == 0:  # Found a trailhead
                total_rating += find_distinct_trails(grid, x, y)

    return total_rating

def main():
    # Read and parse the map
    file_path = "input.txt"
    grid = parse_map(file_path)

    # Calculate the total rating
    total_rating = calculate_total_rating(grid)
    print(f"Total Rating of all Trailheads: {total_rating}")

if __name__ == "__main__":
    main()
