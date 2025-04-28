class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = white = 0
        blue = len(nums)-1

        while white <= blue:
            if nums[white] == 2:
                temp = nums[white]
                nums[white] = nums[blue]
                nums[blue] = temp
                blue -= 1
            elif nums[white] == 1:
                white += 1
            else:
                temp = nums[white]
                nums[white] = nums[red]
                nums[red] = temp
                red += 1
                white += 1
        return nums
        