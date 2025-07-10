class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        l = 0
        window = 1
        res = 0
        for r in range(len(nums)):
            window *= nums[r]
            while window >= k:
                window //= nums[l]
                l += 1
            res += r-l+1
        return res