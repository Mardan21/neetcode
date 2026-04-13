class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # vals = set()
        # for num in nums:
        #     if num in vals:
        #         return num
        #        vals.add(num)
        # return -1

        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                return abs(num)
            nums[idx] *= -1
        
        return -1