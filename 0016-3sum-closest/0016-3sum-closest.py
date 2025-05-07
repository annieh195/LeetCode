class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = inf
        res = 0
        nums.sort()

        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if abs(target - total) < abs(closest):
                    closest = target - total
                    res = total
                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    return target
        return res