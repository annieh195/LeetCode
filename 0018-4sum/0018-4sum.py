class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        l1 = 0
        r1 = len(nums)-1
        nums.sort()
        res = []

        for l1 in range(len(nums)):
            if l1 > 0 and nums[l1] == nums[l1-1]:
                continue
            for r1 in range(len(nums)-1, l1+2, -1):
                if r1 < len(nums)-1 and nums[r1] == nums[r1+1]:
                    continue

                diff1 = target - (nums[l1] + nums[r1])
                l2 = l1+1
                r2 = r1-1
                while l2 < r2:
                    diff2 = nums[l2] + nums[r2]
                    if diff1 == diff2:
                        if [nums[l1], nums[l2], nums[r2], nums[r1]] not in res:
                            res.append([nums[l1], nums[l2], nums[r2], nums[r1]])
                        l2 += 1
                        r2 -= 1
                    elif diff2 < diff1:
                        l2 += 1
                    else:
                        r2 -= 1
        return res