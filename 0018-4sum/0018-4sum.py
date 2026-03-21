class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = set()

        for i in range(n-3):
            for j in range(i+1, n-2): 
                
                l = j+1
                r = n-1
                while l < r:
                    total = nums[l] + nums[r] + nums[i] + nums[j]

                    if total == target:
                        res.add((nums[l], nums[r], nums[i], nums[j]))
                        l += 1
                        r -= 1
                    elif total < target:
                        l += 1
                    else: 
                        r -= 1
        return list(res)