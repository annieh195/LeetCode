class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0 
        res = {}

        for r in range(len(nums)):
            diff = target - nums[r]
            if diff in res:
                return [res[diff], r]
            res[nums[r]] = r