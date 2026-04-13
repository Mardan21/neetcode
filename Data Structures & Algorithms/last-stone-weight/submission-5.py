class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            y = -1 * heapq.heappop(maxHeap)
            x = -1 * heapq.heappop(maxHeap)

            if x != y:
                heapq.heappush(maxHeap, -1 * (y - x))
        
        return -maxHeap[0] if maxHeap else 0
