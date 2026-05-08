class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        summ = sum(nums)
        l = 0

        for i in range(len(nums)):
            r = summ - nums[i]
            if l == r:
                return i
            l += nums[i]
            summ -= nums[i]
        return -1
