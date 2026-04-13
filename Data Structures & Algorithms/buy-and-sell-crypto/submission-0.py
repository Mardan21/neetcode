class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute Force, Time: O(n^2), Space: O(1)
        maxProf = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                currProf = prices[j] - prices[i]
                maxProf = max(currProf, maxProf)

        return maxProf