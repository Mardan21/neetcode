class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        area = 0

        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(grid, r, c, visited))
        
        return area

def dfs(grid, r, c, visited):
    if (r < 0 or 
        c < 0 or 
        r == len(grid) or 
        c == len(grid[0]) or 
        grid[r][c] == 0 or 
        (r, c) in visited):
        return 0
    
    visited.add((r, c))
    return (1 + 
        dfs(grid, r + 1, c, visited) +
        dfs(grid, r - 1, c, visited) +
        dfs(grid, r, c + 1, visited) + 
        dfs(grid, r, c - 1, visited))