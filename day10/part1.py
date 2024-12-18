def read_map_from_file(file_path):
    """Read the topographic map from the input file."""
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

def get_neighbors(x, y, rows, cols):
    """Get valid neighbors of a cell."""
    neighbors = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            neighbors.append((nx, ny))
    return neighbors

def find_trails_and_score(grid):
    """Find all trails and calculate the total score."""
    rows, cols = len(grid), len(grid[0])
    total_score = 0

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == '0':
                visited = set()
                stack = [(x, y, 0)]  # (current_x, current_y, current_height)
                reachable_nines = set()

                while stack:
                    cx, cy, height = stack.pop()

                    if (cx, cy) in visited:
                        continue
                    visited.add((cx, cy))

                    if grid[cx][cy] == '9':
                        reachable_nines.add((cx, cy))
                        continue

                    for nx, ny in get_neighbors(cx, cy, rows, cols):
                        if (nx, ny) not in visited and int(grid[nx][ny]) == height + 1:
                            stack.append((nx, ny, height + 1))

                total_score += len(reachable_nines)

    return total_score

def main():
    file_path = 'input.txt'  # Input file containing the grid
    grid = read_map_from_file(file_path)

    # Calculate the total score
    total_score = find_trails_and_score(grid)

    print(f"Total Score: {total_score}")

if __name__ == "__main__":
    main()
