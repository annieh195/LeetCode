class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxx = 0
        l = 0 
        r = len(height)-1
        while l <= r:
            if height[l] <= height[r]:
                maxx = max(maxx, (r-l)*height[l])
                l += 1
            else:
                maxx = max(maxx, (r-l)*height[r])
                r -= 1
        return maxx
