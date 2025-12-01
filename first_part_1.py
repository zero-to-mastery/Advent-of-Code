def total_distance(left_list, right_list):
    # Sort both lists
    left_list.sort()
    right_list.sort()
    
    # Calculate the total distance
    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))
    return total_distance

# Read input file
file_path = "1st.txt"  # Replace with your file path if different

# Initialize lists
left_list = []
right_list = []

# Parse the input file
with open(file_path, "r") as file:
    for line in file:
        numbers = list(map(int, line.split()))
        if len(numbers) == 2:  # Ensure there are exactly two numbers per line
            left_list.append(numbers[0])
            right_list.append(numbers[1])

# Ensure both lists have the same length
if len(left_list) != len(right_list):
    print("Error: The two lists have different lengths.")
else:
    # Calculate the total distance
    result = total_distance(left_list, right_list)
    print(f"Total Distance: {result}")
