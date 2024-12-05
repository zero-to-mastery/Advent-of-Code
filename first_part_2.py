from collections import Counter

def calculate_similarity_score(left_list, right_list):
    # Count occurrences of each number in the right list
    right_count = Counter(right_list)
    
    # Calculate the similarity score
    similarity_score = 0
    for number in left_list:
        if number in right_count:
            similarity_score += number * right_count[number]
    return similarity_score

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
    # Calculate the similarity score
    similarity_score = calculate_similarity_score(left_list, right_list)
    print(f"Similarity Score: {similarity_score}")
