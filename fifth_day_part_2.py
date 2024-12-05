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

# Reorder an update using topological sorting
def reorder_update(update, rules):
    from collections import defaultdict, deque

    # Build a graph based on the rules
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    # Restrict rules to pages in the update
    update_set = set(update)
    for x, y in rules:
        if x in update_set and y in update_set:
            graph[x].append(y)
            in_degree[y] += 1
            in_degree.setdefault(x, 0)

    # Perform topological sorting
    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_update = []

    while queue:
        node = queue.popleft()
        sorted_update.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_update

def calculate_middle_sum_for_reordered_updates(ordering_rules, update_lists):
    # Check if an update respects all applicable rules
    def is_valid_update(update, rules):
        for x, y in rules:
            if x in update and y in update:
                if update.index(x) > update.index(y):
                    return False
        return True

    incorrectly_ordered = []
    for update in update_lists:
        if not is_valid_update(update, ordering_rules):
            incorrectly_ordered.append(update)

    # Reorder incorrectly ordered updates and calculate the middle sum
    middle_sum = 0
    for update in incorrectly_ordered:
        reordered = reorder_update(update, ordering_rules)
        middle_index = len(reordered) // 2
        middle_sum += reordered[middle_index]

    return middle_sum

# File path to the input
file_path = 'fifth.txt'  # Replace with your actual file path

# Parse the input file
ordering_rules, update_lists = parse_input_file(file_path)

# Calculate the sum of middle page numbers for reordered updates
result = calculate_middle_sum_for_reordered_updates(ordering_rules, update_lists)
print(f"Sum of middle page numbers from reordered updates: {result}")
