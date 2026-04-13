class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROWS, COLS = len(heights), len(heights[0])
        res = []
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = defaultdict()
        pacific = atlantic = False


        def dfs(r, c, prevHeight):
            nonlocal pacific, atlantic
            
            # cell is out of range
            if r < 0 or c < 0:
                pacific = True
                return

            if r == ROWS or c == COLS:
                atlantic = True
                return

            if heights[r][c] > prevHeight:
                return 

            curHeight = heights[r][c]
            heights[r][c] = float('inf')

            for dr, dc in directions:
                dfs(r + dr, c + dc, curHeight)
                if pacific and atlantic:
                    break
            heights[r][c] = curHeight


        for r in range(ROWS):
            for c in range(COLS):
                pacific = False
                atlantic = False
                dfs(r, c, float('inf'))
                if pacific and atlantic:
                    res.append([r, c])

        return res


                        

                


