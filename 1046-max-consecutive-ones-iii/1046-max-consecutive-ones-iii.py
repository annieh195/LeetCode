class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        res = 0
        count = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                count += 1
            while l <= r and count > k:
                l += 1
                if nums[l-1] == 0:
                    count -= 1
            if count <= k:
                res = max(res, r-l+1)
        return res