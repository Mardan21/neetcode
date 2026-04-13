class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # init time and count of fresh fruit

        # perform bfs beginning with rotten fruit
        # init queue to store rotten fruits
        # before turning adjacent fresh fruit rotten, pop the rotten

        # loop through entire grid
        #   if 1, increment freshCount
        #   if 2, append to queue

        # while loop -> cond: rotten fruits exist in queue AND fresh fruit count > 0
        #   define 4 adj. directions -> [r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]
        #   loop thru len(queue) -> len value unchanged until loop finishes -> redef. in next while iteration
        #     loop thru 4 adj. direction cells of the rotten fruit that was popped
        #     if out of bounds, dismiss
        #     if val == 1, set to 2 then append now rotten fruit to queue, then decrement fresh fruit count
        #     
        #   increment time
    
        # return time if freshCount is 0 else return -1

        time, freshCount = 0, 0
        rottenQueue = deque()
        ROWS, COLS = len(grid), len(grid[0])

        # loop through grid
        for r in range(ROWS):
            for c in range(COLS):
                # grid cell is fresh fruit
                if grid[r][c] == 1:
                    freshCount += 1
                # grid cell is rotten fruit
                if grid[r][c] == 2:
                    rottenQueue.append([r, c])

        adjDirections = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while rottenQueue and freshCount > 0:
            for _ in range(len(rottenQueue)):
                r, c = rottenQueue.popleft()
                for dr, dc in adjDirections:
                    row, col = dr + r, dc + c
                    if (row < 0 or row == ROWS or
                       col < 0 or col == COLS or 
                       grid[row][col] != 1):
                       continue
                    grid[row][col] = 2
                    rottenQueue.append([row, col])
                    freshCount -= 1
            time += 1
        
        return time if freshCount == 0 else -1





