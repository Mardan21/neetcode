class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set() # path keeps track of visited cells
        
        # r = current row, c = current column, i = index of letter in word
        def backtrack(r, c, i):
            # valid path was found on prev call
            if i == len(word): 
                return True
            
            # invalid conditions -> r or c out of range, cell already visited, letter not in word
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                word[i] != board[r][c] or (r, c) in path):
                return False
            
            # add the visited path to path set
            path.add((r, c))
            res = (backtrack(r + 1, c, i + 1) or # cell to the right
                backtrack(r - 1, c, i + 1) or    # cell to the left
                backtrack(r, c + 1, i + 1) or    # cell to the top
                backtrack(r, c - 1, i + 1))    # cell to the bottom

            path.remove((r, c))

            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0):
                    return True

        return False