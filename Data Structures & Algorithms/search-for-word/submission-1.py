class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()

        for r in range(rows):
            for c in range(cols):
                if dfs(board, r, c, rows, cols, path, word, 0):
                    return True
        
        return False
        
def dfs(board, r, c, rows, cols, path, word, i):
    if i == len(word):
        return True

    if (r < 0 or
        c < 0 or 
        r >= rows or 
        c >= cols or 
        (r, c) in path or 
        board[r][c] != word[i]):
        return False
    
    path.add((r, c))

    res = (
        dfs(board, r + 1, c, rows, cols, path, word, i + 1) or
        dfs(board, r - 1, c, rows, cols, path, word, i + 1) or
        dfs(board, r, c + 1, rows, cols, path, word, i + 1) or
        dfs(board, r, c - 1, rows, cols, path, word, i + 1)
    )

    path.remove((r, c))

    return res
