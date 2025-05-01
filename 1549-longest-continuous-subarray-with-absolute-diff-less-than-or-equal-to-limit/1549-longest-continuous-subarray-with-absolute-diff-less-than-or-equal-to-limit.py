class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        sl = SortedList()
        res = 0
        l = 0
        
        for r in range(len(nums)):
            sl.add(nums[r])
            while l <= r and sl[-1]-sl[0] > limit:
                sl.discard(nums[l])  
                l += 1
            res = max(res, len(sl))
        return res