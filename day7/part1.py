from itertools import product

def evaluate_expression(numbers, operators):
    """
    Evaluate the expression left-to-right given numbers and operators.
    """
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
    return result

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

def calculate_calibration_result(file_path):
    """
    Calculate the total calibration result for all valid equations.
    """
    equations = parse_input(file_path)
    total = 0
    
    for target, numbers in equations:
        n = len(numbers)
        # Generate all possible combinations of operators
        operator_combinations = product("+-*", repeat=n-1)
        
        # Check if any operator combination matches the target
        valid = False
        for operators in operator_combinations:
            if evaluate_expression(numbers, operators) == target:
                valid = True
                break
        
        if valid:
            total += target
    
    return total

# Example usage
file_path = "input.txt"
result = calculate_calibration_result(file_path)
print(f"Total calibration result: {result}")
