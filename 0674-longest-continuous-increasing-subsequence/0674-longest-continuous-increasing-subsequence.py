class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        l = 0
        stack = [nums[l]]
        res = 1

        for r in range(l+1, len(nums)):
            if nums[r] > stack[-1]:
                stack.append(nums[r])
            else:
                l = r
                stack = [nums[l]]
            res = max(res, len(stack))
        return res
            
            