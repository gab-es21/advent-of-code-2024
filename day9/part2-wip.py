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

def move_files(disk_map):
    """Compact the disk by moving entire files to the leftmost contiguous free space."""
    file_blocks = {}
    # Collect file block ranges
    for i, block in enumerate(disk_map):
        if block != '.':
            file_blocks.setdefault(block, []).append(i)

    # Sort files by file ID in descending order
    sorted_files = sorted(file_blocks.keys(), reverse=True)

    made_move = True
    step_count = 0  # Track the number of steps
    while made_move:
        made_move = False  # Reset move status for each pass
        for file_id in sorted_files:
            blocks = file_blocks[file_id]
            file_length = len(blocks)

            # Find the leftmost free span that can fit the file
            free_start = -1
            free_length = 0
            for i, block in enumerate(disk_map):
                if block == '.':
                    if free_start == -1:
                        free_start = i
                    free_length += 1
                    if free_length >= file_length:
                        break
                else:
                    free_start = -1
                    free_length = 0

            # Move the file if a suitable span is found
            if free_length >= file_length:
                made_move = True
                step_count += 1  # Increment step count
                print(f"Step {step_count}: Moving file ID {file_id}")
                for i in range(file_length):
                    disk_map[free_start + i] = file_id
                for i in blocks:
                    disk_map[i] = '.'
                file_blocks[file_id] = list(range(free_start, free_start + file_length))
                #print(f"  Current Disk Map: {''.join(map(str, disk_map))}")

    print(f"Total steps taken: {step_count}")
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

    # Compact the disk by moving entire files
    compacted_map = move_files(parsed_map)
    print(f"Compacted Map: {''.join(map(str, compacted_map))}")

    # Calculate checksum
    checksum = calculate_checksum(compacted_map)
    print(f"Filesystem Checksum: {checksum}")

if __name__ == "__main__":
    main()
