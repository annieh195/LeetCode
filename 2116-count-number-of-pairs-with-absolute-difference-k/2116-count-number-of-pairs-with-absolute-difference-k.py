class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        res = 0
        mp = defaultdict(int)

        for num in nums:
            mp[num] += 1
            res += mp[k+num] + mp[num-k]
        return res  