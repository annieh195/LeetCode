class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)*2

        if len(nums) == 0:
            return []
        
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i+len(nums)] = ans[i]
        return ans