import re

def extract_and_sum_multiplications(corrupted_memory):
    # Regular expression to match valid mul(X,Y) instructions
    pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"
    
    # Find all matches
    matches = re.findall(pattern, corrupted_memory)
    
    # Calculate the sum of all valid multiplications
    total = 0
    for x, y in matches:
        total += int(x) * int(y)
    
    return total

# Read input file
file_path = "third_part.txt"  # Replace with your file path if different

with open(file_path, "r") as file:
    corrupted_memory = file.read()

# Compute the result
result = extract_and_sum_multiplications(corrupted_memory)
print(f"Total Sum of Valid Multiplications: {result}")
