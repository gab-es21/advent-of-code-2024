from collections import defaultdict, deque

# Parse the input file
file_path = 'input.txt'

print(f"Reading input from: {file_path}")
with open(file_path, 'r') as file:
    data = file.read().strip().split('\n\n')

# First section: ordering rules
ordering_rules = data[0].splitlines()
edges = defaultdict(list)
for rule in ordering_rules:
    x, y = map(int, rule.split('|'))
    edges[x].append(y)

# Second section: updates
updates = [list(map(int, update.split(','))) for update in data[1].splitlines()]

# Function to check if an update is correctly ordered
def is_correctly_ordered(update):
    # Create a subgraph for the current update
    subgraph_edges = defaultdict(list)
    in_degree = defaultdict(int)
    update_set = set(update)

    for x in update:
        in_degree[x] = 0  # Initialize in-degree for all nodes in the update

    for x in update:
        for y in edges[x]:
            if y in update_set:
                subgraph_edges[x].append(y)
                in_degree[y] += 1

    # Perform Kahn's algorithm for topological sort
    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_order = []

    while queue:
        current = queue.popleft()
        sorted_order.append(current)
        for neighbor in subgraph_edges[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check if the sorted order matches the given update
    return sorted_order == update

# Process each update and find the middle page numbers
total_sum = 0
for update in updates:
    if is_correctly_ordered(update):
        middle_index = len(update) // 2
        total_sum += update[middle_index]
        print(f"Update {update} is correctly ordered. Middle page: {update[middle_index]}")
    else:
        print(f"Update {update} is NOT correctly ordered.")

# Final result
print(f"\nTotal sum of middle pages from correctly ordered updates: {total_sum}")
