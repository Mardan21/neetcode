class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # # Brute Force, Time: O(n^2), Space: O(n)
        # res = 0
        # store = set(nums)

        # for num in nums:
        #     streak, curr = 0, num
        #     while curr in store:
        #         streak += 1
        #         curr += 1
        #     res = max(res, streak)
        # return res

        # =========================

        # # Sorting, Time: O(nlogn), Space: O(n)
        # if not nums:
        #     return 0

        # nums.sort()
        # res = 0
        # curr = nums[0]
        # streak = 0
        # i = 0

        # while i < len(nums):
        #     if nums[i] != curr:
        #         curr = nums[i]
        #         streak = 0
        #     while i < len(nums) and nums[i] == curr:
        #         i += 1
        #     streak += 1
        #     curr += 1
        #     res = max(res, streak)
        
        # return res

        # =========================

        # Optimal: HashSet, Time: O(n), Space: O(n)
        numSet = set(nums)
        longest = 0

        for n in numSet:
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(longest, length)

        return longest




