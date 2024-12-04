# Path to the input file
file_path = 'input1.txt'

# Initialize the lists
column1 = []
column2 = []

# Read the file and split the columns
with open(file_path, 'r') as file:
    for line in file:
        # Split the line by 4 spaces
        parts = line.strip().split('   ')  # Note: 4 spaces
        if len(parts) == 2:  # Ensure the line has two columns
            column1.append(int(parts[0]))
            column2.append(int(parts[1]))

# Sort the lists in ascending order
column1.sort()
column2.sort()

# Calculate the positive differences and sum them
differences = [abs(c1 - c2) for c1, c2 in zip(column1, column2)]
total_sum = sum(differences)

# Print results
print("Column 1 (sorted):", column1)
print("Column 2 (sorted):", column2)
print("Differences:", differences)
print("Sum of differences:", total_sum)
