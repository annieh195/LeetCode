class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
            
        a = bisect_left(nums, target)
        b = bisect_right(nums, target)-1
        return [a, b]