from functools import lru_cache

def parse_map(file_path):
    """Read the map from a file and parse it into a 2D grid of integers."""
    with open(file_path, 'r') as file:
        return [list(map(int, line.strip())) for line in file.readlines()]

@lru_cache(None)
def count_trails(grid, x, y):
    """Recursively count distinct hiking trails starting from (x, y)."""
    rows, cols = len(grid), len(grid[0])
    if grid[x][y] == 9:  # A trail ends at height 9
        return 1
    
    total_trails = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            if grid[nx][ny] == grid[x][y] + 1:  # Valid trail step
                total_trails += count_trails(grid, nx, ny)
    
    return total_trails

def compute_trailhead_ratings(grid):
    """Compute the rating (distinct trails) for all trailheads."""
    rows, cols = len(grid), len(grid[0])
    total_rating = 0

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == 0:  # Trailhead found
                total_rating += count_trails(tuple(map(tuple, grid)), x, y)
    
    return total_rating

# Main execution
file_path = "tenth.txt"  
grid = parse_map(file_path)
result = compute_trailhead_ratings(grid)
print("Sum of ratings of all trailheads:", result)
