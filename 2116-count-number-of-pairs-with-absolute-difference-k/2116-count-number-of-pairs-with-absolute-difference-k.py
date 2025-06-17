class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        res = 0
        mp = defaultdict(int)

        for num in nums:
            if num in mp:
                mp[num] += 1
            else:
                mp[num] = 1
            res += mp[k+num] + mp[num-k]
        return res  