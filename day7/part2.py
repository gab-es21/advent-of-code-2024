from itertools import product

def evaluate_with_dp(numbers, target):
    """
    Evaluate if the target can be achieved using dynamic programming.
    """
    n = len(numbers)
    dp = [{} for _ in range(n)]  # dp[i] stores possible results up to index i

    # Base case: First number is the only result
    dp[0][numbers[0]] = ''  # Store expressions as optional debugging info

    # Build DP table
    for i in range(1, n):
        for val, expr in dp[i - 1].items():
            # Add current number with operators
            dp[i][val + numbers[i]] = f"{expr} + {numbers[i]}"
            dp[i][val * numbers[i]] = f"{expr} * {numbers[i]}"
            dp[i][int(str(val) + str(numbers[i]))] = f"{expr} || {numbers[i]}"

    # Check if the target exists in the last DP state
    return target in dp[-1]

def parse_input(file_path):
    """
    Parse the input file and return a list of (target, numbers) tuples.
    """
    equations = []
    with open(file_path, 'r') as file:
        for line in file:
            target, nums = line.strip().split(":")
            target = int(target)
            numbers = list(map(int, nums.split()))
            equations.append((target, numbers))
    return equations

def calculate_calibration_result_dp(file_path):
    """
    Calculate the total calibration result for all valid equations using DP.
    """
    print(f"Parsing input from: {file_path}")
    equations = parse_input(file_path)
    total = 0

    print(f"Processing {len(equations)} equations...")
    for idx, (target, numbers) in enumerate(equations, start=1):
        print(f"Processing equation {idx}: Target = {target}, Numbers = {numbers}")
        if evaluate_with_dp(numbers, target):
            print(f"  - Equation {idx} is valid. Adding {target} to total.")
            total += target
        else:
            print(f"  - Equation {idx} is invalid. Skipping.")

    print(f"Finished processing all equations. Total calibration result: {total}")
    return total

# Example usage
if __name__ == "__main__":
    file_path = "input.txt"  # Replace with your input file path
    result = calculate_calibration_result_dp(file_path)
    print(f"Final Total Calibration Result: {result}")
