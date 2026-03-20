class Solution:
    def rotations(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        self.rotations(nums, 0, n-1)
        self.rotations(nums, 0, k-1)
        self.rotations(nums, k, n-1)
        