class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLS - 1

        while l <= r:
            m = l + (r - l) // 2
            row, col = m // COLS, m % COLS

            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True
        
        return False
        
        # for i in range(len(matrix)):
        #     last_row_val = matrix[i][len(matrix[i]) - 1]
        #     if last_row_val == target:
        #         return True
        #     elif last_row_val > target:
        #         for j in range(len(matrix[i])):
        #             if target == matrix[i][j]:
        #                 return True
        #         return False
        #     else:
        #         continue
        # return False

