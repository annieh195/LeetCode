class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []

        for stone in stones:
            heappush(pq, -stone)

        while len(pq) > 1:
            y = -heappop(pq)
            x = -heappop(pq)

            if y != x:
                heappush(pq, -(y-x))
        return -pq[0] if pq else 0
        