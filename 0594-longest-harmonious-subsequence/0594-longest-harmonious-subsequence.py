class Solution:
    def findLHS(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        res = 0

        for num in nums:
            mp[num] += 1

        for key in mp.keys():
            if (key+1) in mp:
                res = max(res, mp[key]+mp[key+1])
        return res