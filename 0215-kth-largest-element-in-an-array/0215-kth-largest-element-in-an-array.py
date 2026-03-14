class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []

        for num in nums:
            heappush(pq, -num)
        
        while k != 1:
            heappop(pq)
            k -= 1
        return -pq[0]