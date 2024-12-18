from itertools import combinations

def read_map(file_path):
    """Read the map from the input file."""
    with open(file_path, 'r') as f:
        return [line.strip() for line in f]

def find_antennas(grid):
    """Find the positions of all antennas for each frequency."""
    antennas = {}
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char != '.':
                antennas.setdefault(char, []).append((r, c))
    return antennas

def calculate_extended_antinodes(antenna_positions, max_extension):
    """Calculate all antinodes for a specific frequency with extended vectors."""
    antinodes = set(antenna_positions)  # Include original antennas as antinodes
    for (r1, c1), (r2, c2) in combinations(antenna_positions, 2):
        # Compute the vector (dr, dc)
        dr, dc = r2 - r1, c2 - c1
        for t in range(1, max_extension + 1):  # Extend up to max_extension times
            antinode1 = (r1 - t * dr, c1 - t * dc)
            antinode2 = (r2 + t * dr, c2 + t * dc)
            antinodes.update([antinode1, antinode2])
    return antinodes

def filter_valid_antinodes(grid, antinodes):
    """Filter antinodes that fall within the grid bounds."""
    valid_antinodes = set()
    max_rows, max_cols = len(grid), len(grid[0])
    for r, c in antinodes:
        if 0 <= r < max_rows and 0 <= c < max_cols:
            valid_antinodes.add((r, c))
    return valid_antinodes


def count_antinodes_per_letter(grid, antennas):
    """Count antinodes for each frequency and sum overlaps separately."""
    max_extension = max(len(grid), len(grid[0]))  # Set extension limit
    letter_antinodes_count = {}
    all_antinodes = set()
    for frequency, positions in antennas.items():
        print(f"Processing frequency '{frequency}' with {len(positions)} antennas...")
        antinodes = calculate_extended_antinodes(positions, max_extension)
        valid_antinodes = filter_valid_antinodes(grid, antinodes)
        letter_antinodes_count[frequency] = len(valid_antinodes)
        all_antinodes.update(valid_antinodes)
    return letter_antinodes_count, len(all_antinodes)

def main():
    file_path = 'input.txt'
    print(f"Reading map from {file_path}...")
    grid = read_map(file_path)

    print("Finding antennas for each frequency...")
    antennas = find_antennas(grid)

    print("Counting antinodes for each frequency...")
    letter_antinodes_count, total_unique_antinodes = count_antinodes_per_letter(grid, antennas)

    print("\nAntinodes Count Per Letter:")
    for letter, count in letter_antinodes_count.items():
        print(f"  {letter}: {count}")

    print(f"\nTotal unique antinodes (including overlaps): {total_unique_antinodes}")

if __name__ == "__main__":
    main()
