class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = [0]*(len(nums)+1)

        for i in range(1, len(nums)+1):
            prefix[i] = prefix[i-1] + nums[i-1]
        
        mp = defaultdict(int)
        for r in range(len(prefix)):
            mod = prefix[r]%k
            if mod in mp: 
                if r-mp[mod] >= 2:
                    return True
            else:
                mp[mod] = r
        return False    