class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0]*(len(nums)+1)
        res = 0

        for i in range(1, len(nums)+1):
            prefix[i] = prefix[i-1] + nums[i-1]
        
        count = defaultdict(int)
        for r in range(len(prefix)-1):
            count[prefix[r]] += 1
            res += count[prefix[r+1]-k]
        return res
        

        return res