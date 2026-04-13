class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # loop through the array
        # at each index i, calc the difference (the value we are looking for)
        # map the index to required value

        values = {}

        for i, val in enumerate(nums):
            difference = target - val

            if difference in values:
                return [values[difference], i]

            values[val] = i

            


        