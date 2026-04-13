class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # add open parentheses to stack if open_p < n
        # add closing parentheses to stack if close_p < open_p
        # parenthesis combo is valid IFF open_p == close_p == n
        
        stack, res = [], []

        # open_p -> num of open parentheses
        # close_p -> num of closing parentheses
        def backtrack(open_paren, closed_paren):
            if open_paren == closed_paren == n:
                res.append(''.join(stack))
                return

            if open_paren < n:
                stack.append('(')
                backtrack(open_paren + 1, closed_paren)
                stack.pop()
            
            if closed_paren < open_paren:
                stack.append(')')
                backtrack(open_paren, closed_paren + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res


