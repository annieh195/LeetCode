class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        
        for num in nums:
            if res and res[-1][-1] == num-1:
                res[-1].append(num)
            else:
                res.append([num])

        resRange = []
        for r in res:
            if len(r) == 1:
                resRange.append(str(r[0]))
            else:
                resRange.append(str(r[0]) + "->" + str(r[-1]))
        return resRange    