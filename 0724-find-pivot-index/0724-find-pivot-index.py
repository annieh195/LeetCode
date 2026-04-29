class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = 0

        while l < len(nums):
            if (l == 0 and sum(nums[1:len(nums)]) == 0) or (l == len(nums) and sum(nums[:len(nums)-1]) == 0):
                return 0
            if sum(nums[:l]) == sum(nums[l+1:]):
                return l
            else:
                l += 1
        return -1
