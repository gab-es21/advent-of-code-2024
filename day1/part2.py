# Path to the input file
file_path = 'input1.txt'

# Initialize the lists
left_list = []
right_list = []

print(f"Opening the file: {file_path}")

# Read the file and split the columns
with open(file_path, 'r') as file:
    print("Reading the file line by line...")
    for line_number, line in enumerate(file, start=1):
        print(f"Line {line_number}: {line.strip()}")  # Show the line being read
        # Split the line by any whitespace
        parts = line.strip().split()
        if len(parts) == 2:  # Ensure the line has two columns
            try:
                left_list.append(int(parts[0]))
                right_list.append(int(parts[1]))
                print(f"Parsed: {parts[0]} (Left), {parts[1]} (Right)")
            except ValueError:
                print(f"Warning: Skipping invalid data on line {line_number}")
        else:
            print(f"Warning: Line {line_number} does not have exactly two columns after splitting")

print("Finished reading the file.")
print(f"Left List: {left_list}")
print(f"Right List: {right_list}")

# Calculate the frequency of each number in the right list
from collections import Counter

right_frequency = Counter(right_list)
print(f"Frequencies in Right List: {right_frequency}")

# Compute the similarity score
similarity_score = 0

for number in left_list:
    count_in_right = right_frequency.get(number, 0)  # Get the count or 0 if the number is not in the right list
    contribution = number * count_in_right
    similarity_score += contribution
    print(f"Number: {number}, Count in Right List: {count_in_right}, Contribution: {contribution}")

# Final similarity score
print("\nProcess complete.")
print(f"Similarity Score: {similarity_score}")
