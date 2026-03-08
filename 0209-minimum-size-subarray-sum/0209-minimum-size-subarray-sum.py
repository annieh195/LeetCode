class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        window = 0
        res = float('inf')

        for r in range(len(nums)):
            window += nums[r]
            while window >= target:
                res = min(res, r-l+1)
                window -= nums[l]
                l += 1
        return res if res != float('inf') else 0