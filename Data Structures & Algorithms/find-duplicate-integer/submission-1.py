class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # vals = set()
        # for num in nums:
        #     if num in vals:
        #         return num
        #     else:
        #         vals.add(num)

        # return
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]
        return -1