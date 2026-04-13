class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res, heap = [], []
        heapq.heapify(heap)

        for i, p in enumerate(points):
            distance = math.sqrt((p[0] - 0)**2 + (p[1] - 0)**2)
            heapq.heappush(heap, (distance, i))

        while len(res) < k:
            distPlusIdx = heapq.heappop(heap)
            res.append(points[distPlusIdx[1]])

        return res