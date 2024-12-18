def parse_disk_map(disk_map):
    """Parse the input disk map into a list representing files and free space."""
    parsed_map = []
    file_id = 0
    is_file = True

    for length in map(int, disk_map):
        if is_file:
            parsed_map.extend([file_id] * length)
            file_id += 1
        else:
            parsed_map.extend(['.'] * length)
        is_file = not is_file

    return parsed_map

def compact_disk(disk_map):
    """Simulate the compaction process of moving file blocks to the left."""
    while '.' in disk_map:
        # Find the first free space and the last file block
        leftmost_free = disk_map.index('.')
        rightmost_file = len(disk_map) - 1 - disk_map[::-1].index(next(f for f in reversed(disk_map) if f != '.'))

        if rightmost_file < leftmost_free:
            break

        # Move the file block
        disk_map[leftmost_free], disk_map[rightmost_file] = disk_map[rightmost_file], '.'

    return disk_map

def calculate_checksum(disk_map):
    """Calculate the filesystem checksum based on the compacted disk map."""
    checksum = 0
    for position, block in enumerate(disk_map):
        if block != '.':
            checksum += position * block
    return checksum

def main():
    # Read input
    with open("input.txt", "r") as file:
        disk_map = file.read().strip()

    print(f"Original Disk Map: {disk_map}")

    # Parse the disk map
    parsed_map = parse_disk_map(disk_map)
    print(f"Parsed Map: {''.join(map(str, parsed_map))}")

    # Compact the disk
    compacted_map = compact_disk(parsed_map)
    print(f"Compacted Map: {''.join(map(str, compacted_map))}")

    # Calculate checksum
    checksum = calculate_checksum(compacted_map)
    print(f"Filesystem Checksum: {checksum}")

if __name__ == "__main__":
    main()
