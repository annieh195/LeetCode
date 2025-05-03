class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            if res[-1][1] >= intervals[i][0]:
                [a,b] = res.pop()
                res.append([a, max(b, intervals[i][1])])
            else:
                res.append(intervals[i])
        return res
