class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            cur.append(nums[i]) # including num[i] in cur target combo []
            dfs(i, cur, total + nums[i]) # 1st rec. call -> including nums[i]
            cur.pop() # clean up cur target combo [] for 2nd rec. call
            dfs(i + 1, cur, total) # 2nd rec. call -> skip nums[i] -> go to nums[i+1]

        dfs(0, [], 0)
        return res
