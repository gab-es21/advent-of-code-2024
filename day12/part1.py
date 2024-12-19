def calculate_fencing_price(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    total_price = 0

    def flood_fill(r, c, plant_type):
        """Flood-fill to find the region, calculate area and perimeter."""
        stack = [(r, c)]
        visited[r][c] = True
        area = 0
        perimeter = 0

        while stack:
            x, y = stack.pop()
            area += 1
            local_perimeter = 4

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    if grid[nx][ny] == plant_type:
                        local_perimeter -= 1
                        if not visited[nx][ny]:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
            perimeter += local_perimeter

        return area, perimeter

    # Iterate through the grid to find regions
    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                area, perimeter = flood_fill(r, c, grid[r][c])
                total_price += area * perimeter

    return total_price

def main():
    # Read input from input.txt
    with open("input.txt", "r") as file:
        grid = [list(line.strip()) for line in file.readlines()]

    # Calculate total fencing price
    total_price = calculate_fencing_price(grid)
    print(f"Total Price of Fencing: {total_price}")

if __name__ == "__main__":
    main()
