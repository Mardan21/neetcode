class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        res = []

        def dfs(i, cur_combo, total):
            if total == target:
                if not (cur_combo in res):
                    res.append(cur_combo.copy())
            if total > target or i >= len(candidates):
                return
            
            cur_combo.append(candidates[i])
            dfs(i + 1, cur_combo, total + candidates[i])
            cur_combo.pop()
            dfs(i + 1, cur_combo, total)
        
        dfs(0, [], 0)
        return res
                