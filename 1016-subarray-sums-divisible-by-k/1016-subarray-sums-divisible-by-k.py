class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        prefix = [0]*(len(nums)+1)
        mp = defaultdict(int)

        for i in range(1, len(nums)+1):
            prefix[i] = prefix[i-1] + nums[i-1]
        
        for r in range(len(prefix)-1):
            mp[prefix[r]%k] += 1 
            res += mp[prefix[r+1]%k]
        return res