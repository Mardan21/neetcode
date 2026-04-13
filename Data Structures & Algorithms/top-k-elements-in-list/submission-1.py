class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # Brute Force, Time: O(nlogn), Space: O(n)
        # counts = {}
        # for val in nums:
        #     counts[val] = counts.get(val, 0) + 1

        # arr = []
        # for num, count in counts.items():
        #     arr.append([count, num])
        # arr.sort()

        # res = []
        # while len(res) < k:
        #     res.append(arr.pop()[1])
        # return res

        # ==================================

        # # Min-Heap, Time: O(nlogk), Space: O(n + k)
        # heap = []
        # counts = {}
        # for num in nums:
        #     counts[num] = 1 + counts.get(num, 0)
        
        # for num in counts.keys():
        #     heapq.heappush(heap, (counts[num], num))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
            
        # res = []
        # for i in range(k):
        #     res.append(heapq.heappop(heap)[1])
        # return res

        # ==================================

        # Bucket Sort, Time: O(n), Space: O(n)
        freq = [[] for i in range(len(nums) + 1)]
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        for num, count in counts.items():
            freq[count].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res


