class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        count = [0]*len(nums)
        for i in range(len(nums)):
            if nums[i] % modulo == k:
                count[i] = 1
            else:
                count[i] = 0
        
        prefix = [0]
        for i in range(len(count)):
            prefix.append(prefix[i]+count[i])

        mp = defaultdict(int)
        res = 0
        for r in range(len(nums)):
            mp[prefix[r]%modulo] += 1
            res += mp[(prefix[r+1] + modulo - k)%modulo]
        return res