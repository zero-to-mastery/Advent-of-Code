from collections import deque

def parse_map(file_path):
    """Read the map from a file and parse it into a 2D grid of integers."""
    with open(file_path, 'r') as file:
        return [list(map(int, line.strip())) for line in file.readlines()]

def bfs(grid, start):
    """Perform BFS to find reachable height-9 positions."""
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([start])
    visited = set()
    reachable_nines = set()

    while queue:
        x, y = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        
        # If height is 9, add to reachable nines
        if grid[x][y] == 9:
            reachable_nines.add((x, y))
            continue
        
        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                if grid[nx][ny] == grid[x][y] + 1:  # Valid hiking trail step
                    queue.append((nx, ny))
    
    return reachable_nines

def compute_trailhead_scores(grid):
    """Compute the score for all trailheads in the map."""
    rows, cols = len(grid), len(grid[0])
    total_score = 0

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == 0:  # Trailhead found
                reachable_nines = bfs(grid, (x, y))
                total_score += len(reachable_nines)
    
    return total_score

# Main execution
file_path = "tenth.txt" 
grid = parse_map(file_path)
result = compute_trailhead_scores(grid)
print("Sum of scores of all trailheads:", result)
