class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # store result and current partition
        res = []
        part = []

        # define our dfs function to do the backtracking 
        # this includes the palindrome checker
        def dfs(i):
            # base case -> if reached end of string
            if i >= len(s):
                res.append(part.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    part.append(s[i: j + 1])

                    # partition remaining string from j + 1 since s[i: j + 1] in part
                    dfs(j + 1)
                    
                    # remove choice & try other options -> j moves to next index in for loop
                    part.pop()

        # call the dfs function and return
        dfs(0)
        return res


    # define palindrome checking helper function -> two pointer algo
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True
        