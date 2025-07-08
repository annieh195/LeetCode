class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        l = 0
        window = 0

        for r in range(len(nums)):
            window += nums[r]
            while window >= target:
                res = min(res, r-l+1)
                window -= nums[l]
                l += 1

        return res if res != float('inf') else 0