class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        summ = nums[0]
        for i in range(1, len(nums)):
            summ += nums[i]
            nums[i] = summ
        return nums