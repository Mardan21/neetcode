class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r # greatest value that k can be

        while l <= r:
            k = (l + r) // 2 # midpoint of l and r ptr
            eat_time = 0
            for p in piles:
                eat_time += math.ceil(p / k)
            if eat_time <= h:
                r = k - 1
                res = min(res, k)
            else:
                l = k + 1
        
        return res
            

