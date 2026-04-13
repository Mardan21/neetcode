class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # add open parentheses to stack if open_p < n
        # add closing parentheses to stack if close_p < open_p
        # parenthesis combo is valid IFF open_p == close_p == n
        
        stack, res = [], []

        # open_p -> num of open parentheses
        # close_p -> num of closing parentheses
        def backtrack(open_count, close_count):
            if open_count == close_count == n:
                res.append(''.join(stack))
                return

            if open_count < n:
                stack.append('(')
                backtrack(open_count + 1, close_count)
                stack.pop()
            
            if close_count < open_count:
                stack.append(')')
                backtrack(open_count, close_count + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res


