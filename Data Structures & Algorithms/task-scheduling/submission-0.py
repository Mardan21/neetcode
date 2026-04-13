class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxHeap = [-cnt for cnt in freq.values()]
        heapq.heapify(maxHeap)

        time = 0
        queue = deque() # (count, available_at_time)

        while queue or maxHeap:
            time += 1

            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1 # pop from heap and decrement count
                if cnt < 0: # we still have remaining tasks for this
                    queue.append((cnt, time + n))

            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])

        return time


