class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return bisect_left(nums, target)
        else:
            return bisect_right(nums, target)