class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx = 0
        res = 0
        for num in nums:
            if num == 1:
                maxx += 1
                res = max(maxx, res)
            else:
                maxx = 0
        return res