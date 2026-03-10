class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)

        for num in nums:
            mp[num] += 1

        pq = []
        res = []

        for num, freq in mp.items():
            heappush(pq, [-freq, num])
        
        while len(res) < k:
            res.append(heappop(pq)[1])
        return res
