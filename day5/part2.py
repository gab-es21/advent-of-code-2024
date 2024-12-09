from collections import defaultdict, deque

# Input file path
file_path = "input.txt"

# Parse the input
print(f"Reading the input from: {file_path}")
with open(file_path, 'r') as file:
    lines = file.read().strip().split("\n")

# Separate rules and updates
rules = []
updates = []
parsing_rules = True
for line in lines:
    if "|" in line:
        rules.append(tuple(map(int, line.split("|"))))
    elif "," in line:
        updates.append(list(map(int, line.split(","))))

# Create the graph for ordering rules
graph = defaultdict(list)
in_degree = defaultdict(int)
all_pages = set()
for x, y in rules:
    graph[x].append(y)
    in_degree[y] += 1
    all_pages.update([x, y])

# Function to check if an update is in the correct order
def is_correct_order(update):
    index_map = {page: i for i, page in enumerate(update)}
    for x, y in rules:
        if x in index_map and y in index_map and index_map[x] > index_map[y]:
            return False
    return True

# Function to topologically sort an update according to the rules
def topological_sort(update):
    subgraph = defaultdict(list)
    sub_in_degree = defaultdict(int)
    for x, y in rules:
        if x in update and y in update:
            subgraph[x].append(y)
            sub_in_degree[y] += 1
    
    # Add nodes with no incoming edges
    queue = deque([node for node in update if sub_in_degree[node] == 0])
    sorted_order = []
    
    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        for neighbor in subgraph[node]:
            sub_in_degree[neighbor] -= 1
            if sub_in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_order

# Part 1: Identify correctly ordered updates and calculate their middle pages
correct_sum = 0
incorrect_updates = []

for update in updates:
    if is_correct_order(update):
        middle_page = update[len(update) // 2]
        correct_sum += middle_page
    else:
        incorrect_updates.append(update)

#print(f"Part 1: Sum of middle pages for correctly ordered updates: {correct_sum}")

# Part 2: Correct the order of incorrect updates and calculate their middle pages
incorrect_sum = 0

for update in incorrect_updates:
    sorted_update = topological_sort(update)
    middle_page = sorted_update[len(sorted_update) // 2]
    incorrect_sum += middle_page

print(f"Part 2: Sum of middle pages for corrected updates: {incorrect_sum}")
