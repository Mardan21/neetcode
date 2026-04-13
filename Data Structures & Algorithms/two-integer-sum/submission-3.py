class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}

        for i, val in enumerate(nums):
            difference = target - val

            if difference in values:
                return [values[difference], i]

            values[val] = i

            


        