class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        summ = 0
        mp = {0:-1}
        for r in range(len(nums)):
            summ += nums[r]
            mod = summ%k
            if mod in mp: 
                if r-mp[mod] >= 2:
                    return True
            else:
                mp[mod] = r
        return False    