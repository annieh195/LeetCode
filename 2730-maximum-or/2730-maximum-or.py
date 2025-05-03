class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        n = len(nums)
        preOr = [0]*n
        surOr = [0]*n
        surOr[-1] = nums[-1]
        preOr[0] = nums[0]

        for i in range(1, n):
            preOr[i] = preOr[i-1] | nums[i]
        
        for i in range(n-2, -1, -1):
            surOr[i] = surOr[i+1] | nums[i]

        maxx = 0
        for i in range(n):
            l = r = 0
            if i-1 >= 0:
                l = preOr[i-1]
            if i+1 < n:
                r = surOr[i+1]
    
            maxx = max(maxx, l | nums[i]<<k | r)
        return maxx