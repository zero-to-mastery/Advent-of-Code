import re

def process_corrupted_memory(corrupted_memory):
    # Regex patterns
    mul_pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"  # Matches valid mul(X,Y)
    do_pattern = r"do\(\)"  # Matches do()
    dont_pattern = r"don't\(\)"  # Matches don't()

    # State variable
    mul_enabled = True
    total = 0

   
    tokens = re.split(r"(\bmul\(\s*\d+\s*,\s*\d+\s*\)|do\(\)|don't\(\))", corrupted_memory)

    for token in tokens:
        token = token.strip()
        if not token:
            continue
        
        if re.match(do_pattern, token):
            mul_enabled = True
        elif re.match(dont_pattern, token):
            mul_enabled = False
        elif mul_enabled and re.match(mul_pattern, token):
            # Extract numbers from the valid mul instruction
            x, y = map(int, re.findall(r"\d+", token))
            total += x * y

    return total

# Read input file
file_path = "third_part.txt"  # Replace with your file path if different

with open(file_path, "r") as file:
    corrupted_memory = file.read()

# Compute the result
result = process_corrupted_memory(corrupted_memory)
print(f"Total Sum of Enabled Multiplications: {result}")
