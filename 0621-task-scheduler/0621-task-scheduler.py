class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = [-cnt for cnt in Counter(tasks).values()]
        heapq.heapify(maxHeap)
        
        time = 0
        pq = deque()
        while maxHeap or pq:
            time += 1
            if not maxHeap:
                time = pq[0][1]
            else:
                task = 1 + heapq.heappop(maxHeap)
                if task:
                    pq.append([task, time + n])
            if pq and pq[0][1] == time:
                heapq.heappush(maxHeap, pq.popleft()[0])
        return time