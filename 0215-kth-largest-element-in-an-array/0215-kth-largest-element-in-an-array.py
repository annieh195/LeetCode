class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        res = 0

        for num in nums:
            heappush(pq, -num)
        
        while k:
            res = -heappop(pq)
            k -= 1
        return res