# Path to the input file
file_path = 'input1.txt'

def is_safe(report):
    """
    Determines if a report is safe based on the rules:
    1. Levels must all be either increasing or decreasing.
    2. Any two adjacent levels must differ by at least 1 and at most 3.
    """
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]
    
    # Check if differences are either all positive or all negative
    all_increasing = all(1 <= diff <= 3 for diff in differences)
    all_decreasing = all(-3 <= diff <= -1 for diff in differences)
    
    # Return True if the report is safe
    return all_increasing or all_decreasing

# Read the input file
print(f"Opening the file: {file_path}")
with open(file_path, 'r') as file:
    reports = [list(map(int, line.strip().split())) for line in file]

# Determine how many reports are safe
safe_count = 0
for i, report in enumerate(reports, start=1):
    if is_safe(report):
        print(f"Report {i}: {report} is SAFE")
        safe_count += 1
    else:
        print(f"Report {i}: {report} is UNSAFE")

# Final output
print(f"\nTotal number of safe reports: {safe_count}")
