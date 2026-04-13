class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # check last index of current row
        #   if its equal to target, return true
        #   elif its greater than target, only look through this row
        #   else continue -> go to next row

        for i in range(len(matrix)):
            last_row_val = matrix[i][len(matrix[i]) - 1]
            if last_row_val == target:
                return True
            elif last_row_val > target:
                for j in range(len(matrix[i])):
                    if target == matrix[i][j]:
                        return True
                return False
            else:
                continue
        return False

