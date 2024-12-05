def count_word_occurrences(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_length = len(word)
    count = 0

    # Helper function to check if the word matches in a given direction
    def match_at_direction(x, y, dx, dy):
        for i in range(word_length):
            nx, ny = x + i * dx, y + i * dy
            if not (0 <= nx < rows and 0 <= ny < cols) or grid[nx][ny] != word[i]:
                return False
        return True

    # Iterate over every cell in the grid
    for x in range(rows):
        for y in range(cols):
            # Check all 8 possible directions
            directions = [
                (0, 1),   # Horizontal right
                (0, -1),  # Horizontal left
                (1, 0),   # Vertical down
                (-1, 0),  # Vertical up
                (1, 1),   # Diagonal top-left to bottom-right
                (-1, -1), # Diagonal bottom-right to top-left
                (1, -1),  # Diagonal top-right to bottom-left
                (-1, 1)   # Diagonal bottom-left to top-right
            ]
            for dx, dy in directions:
                if match_at_direction(x, y, dx, dy):
                    count += 1

    return count

# Read input file
file_path = "fourth.txt"  # Replace with your file path if different

# Parse the grid from the file
with open(file_path, "r") as file:
    grid = [list(line.strip()) for line in file]

# Count occurrences of "XMAS"
word = "XMAS"
occurrences = count_word_occurrences(grid, word)
print(f"Total occurrences of '{word}': {occurrences}")
