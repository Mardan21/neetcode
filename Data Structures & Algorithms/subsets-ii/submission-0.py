class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        valid_subsets = set()

        def backtrack(i, subset):
            if i == len(nums):
                valid_subsets.add(tuple(subset))
                return

            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()
            backtrack(i+1, subset)

        nums.sort()
        backtrack(0, [])

        return [list(s) for s in valid_subsets]