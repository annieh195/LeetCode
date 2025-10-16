class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        summ = 0
        res = inf

        for r in range(len(nums)):
            summ += nums[r]
            while summ >= target:
                res = min(res, r-l+1)
                summ -= nums[l]
                l += 1
        return res if res != inf else 0