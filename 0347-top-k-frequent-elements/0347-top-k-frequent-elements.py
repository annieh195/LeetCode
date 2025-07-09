class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        for num in nums:
            mp[num] += 1
        
        pq = []
        res = []
        for key, value in mp.items():
            heappush(pq, [-value, key])
        
        while k:
            value, key = heappop(pq)
            res.append(key)
            k -= 1
        return res