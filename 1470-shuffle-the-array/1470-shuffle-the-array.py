class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l = 0
        r = n
        ans = [0]*len(nums)

        for i in range(len(nums)):
            if i % 2 == 0:
                ans[i] = nums[l]
                l += 1
            else:
                ans[i] = nums[r]
                r += 1
        return ans