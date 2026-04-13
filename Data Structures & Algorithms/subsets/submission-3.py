class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        # res starts at [[]]
        # num = 1 -> res = [[], [1]]
        # num = 2 -> res = [[], [1], [2], [1, 2]]
        # num = 3 -> res = [[], [1], [2], [1, 2], [1, 3], [1, 2, 3]]

        for num in nums:
            res += [subset + [num] for subset in res]
        return res

