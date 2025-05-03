class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        n = len(nums)
        preSum = [0]*n
        surSum = [0]*n
        surSum[-1] = nums[-1]
        preSum[0] = nums[0]

        for i in range(1, n):
            preSum[i] = preSum[i-1] | nums[i]
        
        for i in range(n-2, -1, -1):
            surSum[i] = surSum[i+1] | nums[i]

        maxx = 0
        for i in range(n):
            l = r = 0
            if i-1 >= 0:
                l = preSum[i-1]
            if i+1 < n:
                r = surSum[i+1]
    
            maxx = max(maxx, l | nums[i]<<k | r)
        return maxx