# Parse the input file content
def parse_input_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Split the content into rules and updates sections
    sections = content.strip().split("\n\n")
    rules = sections[0].split("\n")
    updates = sections[1].split("\n")

    # Parse rules into a list of tuples
    ordering_rules = []
    for rule in rules:
        x, y = map(int, rule.split("|"))
        ordering_rules.append((x, y))

    # Parse updates into lists of integers
    update_lists = [list(map(int, update.split(","))) for update in updates]

    return ordering_rules, update_lists

# Function to calculate the sum of middle page numbers for valid updates
def calculate_middle_sum(ordering_rules, update_lists):
    # Check if an update respects all applicable rules
    def is_valid_update(update, rules):
        for x, y in rules:
            if x in update and y in update:
                if update.index(x) > update.index(y):
                    return False
        return True

    # Validate updates
    valid_updates = [update for update in update_lists if is_valid_update(update, ordering_rules)]

    # Calculate the middle page number sum
    middle_sum = 0
    for update in valid_updates:
        middle_index = len(update) // 2
        middle_sum += update[middle_index]

    return middle_sum

# File path to the input
file_path = 'fifth.txt'  # Replace with your actual file path

# Parse the input file
ordering_rules, update_lists = parse_input_file(file_path)

# Calculate and print the result
result = calculate_middle_sum(ordering_rules, update_lists)
print(f"Sum of middle page numbers from valid updates: {result}")
