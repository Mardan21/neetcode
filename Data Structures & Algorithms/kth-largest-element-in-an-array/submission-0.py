class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        heapq.heapify(maxHeap)
        for n in nums:
            if len(maxHeap) < k:
                heapq.heappush(maxHeap, n)
            elif -n < -maxHeap[0]:
                heapq.heapreplace(maxHeap, n)
        return maxHeap[0]
