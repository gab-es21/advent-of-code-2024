from collections import defaultdict

def parse_input(file_path):
    with open(file_path, "r") as file:
        return [list(line.strip()) for line in file]

def find_regions(garden_map):
    """Identify all regions in the garden map and return their areas and adjacency info."""
    rows, cols = len(garden_map), len(garden_map[0])
    visited = [[False] * cols for _ in range(rows)]
    regions = defaultdict(list)

    def dfs(r, c, region_type):
        stack = [(r, c)]
        current_region = []

        while stack:
            x, y = stack.pop()
            if 0 <= x < rows and 0 <= y < cols and not visited[x][y] and garden_map[x][y] == region_type:
                visited[x][y] = True
                current_region.append((x, y))
                stack.extend([(x + dx, y + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]])

        return current_region

    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                region_type = garden_map[r][c]
                region_cells = dfs(r, c, region_type)
                if region_cells:
                    regions[region_type].append(region_cells)

    return regions

def calculate_perimeter(region, garden_map):
    """Calculate the perimeter of a region based on exposed edges."""
    perimeter = 0
    for x, y in region:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= len(garden_map) or ny >= len(garden_map[0]) or garden_map[nx][ny] != garden_map[x][y]:
                perimeter += 1
    return perimeter

def calculate_sides(region):
    """Calculate the number of distinct fence sides for a region."""
    sides = set()
    for x, y in region:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (x, y, nx, ny) not in sides and (nx, ny, x, y) not in sides:
                sides.add((x, y, nx, ny))
    return len(sides)

def calculate_total_price(garden_map, use_sides=False):
    regions = find_regions(garden_map)
    total_price = 0

    for plant_type, region_list in regions.items():
        for region in region_list:
            area = len(region)
            if use_sides:
                sides = calculate_sides(region)
                price = area * sides
            else:
                perimeter = calculate_perimeter(region, garden_map)
                price = area * perimeter
            total_price += price

    return total_price

def main():
    file_path = "input.txt"
    garden_map = parse_input(file_path)

    # Part 1: Perimeter-based pricing
    total_price_part1 = calculate_total_price(garden_map, use_sides=False)
    print(f"Total price (Part 1): {total_price_part1}")

    # Part 2: Sides-based pricing
    total_price_part2 = calculate_total_price(garden_map, use_sides=True)
    print(f"Total price (Part 2): {total_price_part2}")

if __name__ == "__main__":
    main()