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
                dist = abs(target - total)
                if dist < closest:
                    closest = min(closest, dist)
                    res = total
                if target == total:
                    return target
                elif total < target:
                    l += 1
                else:
                    r -= 1
        return res