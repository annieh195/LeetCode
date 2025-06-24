class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = 0
        sl = SortedList()
        l = 0

        for r in range(len(nums)):
            sl.add(nums[r])
            while sl[-1]-sl[0] > limit:
                sl.discard(nums[l])
                l += 1
            res = max(res, r-l+1)
        return res
