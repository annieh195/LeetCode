class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0]*(len(nums)+1)

        for i in range(len(nums)):
            prefix[i+1] = prefix[i] + nums[i]
        print(prefix)
        count = defaultdict(int)
        res = 0 
        for r in range(len(prefix)-1):
            count[prefix[r]] += 1
            res += count[prefix[r+1]-k]
        return res 
