class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        window = 0
        ans = float("-inf")

        for r in range(len(nums)):
            window += nums[r]
            if r-l+1 > k:
                window -= nums[l]
                l += 1
            if r-l+1 == k:
                ans = max(ans, window/k)

        return ans