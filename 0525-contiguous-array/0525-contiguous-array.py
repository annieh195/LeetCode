class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        pre0 = [0]*len(nums)
        pre0[0] = 1 if nums[0] == 0 else 0
        pre1 = [0]*len(nums)
        pre1[0] = 1 if nums[0] == 1 else 0
        mp = defaultdict(int)
        mp[0] = -1
        res = 0

        for i in range(1, len(nums)):
            if nums[i] == 0:
                pre0[i] = pre0[i-1] + 1
                pre1[i] = pre1[i-1]
            else:
                pre0[i] = pre0[i-1]
                pre1[i] = pre1[i-1] + 1
        
        for r in range(len(nums)):
            if pre0[r] - pre1[r] not in mp:
                mp[pre0[r] - pre1[r]] = r
            l = mp[pre0[r] - pre1[r]] + 1
            res = max(res, r-l+1)
        return res