class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0: # gate
                    q.append([r, c])
                    visited.add((r, c))

        gateDist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = gateDist

                self.addRoom(r + 1, c, grid, visited, q)
                self.addRoom(r - 1, c, grid, visited, q)
                self.addRoom(r, c + 1, grid, visited, q)
                self.addRoom(r, c - 1, grid, visited, q)

            gateDist += 1

    def addRoom(self, r, c, grid, visited, q):
        if (r < 0 or r == len(grid) or c < 0 or c == len(grid[0]) or (r, c) in visited or grid[r][c] == -1):
            return
        
        visited.add((r, c))
        q.append([r, c])

