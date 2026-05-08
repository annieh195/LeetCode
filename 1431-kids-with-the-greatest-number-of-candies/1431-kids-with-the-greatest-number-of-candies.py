class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        curMax = max(candies)
        res = []
        for num in candies:
            if num + extraCandies >= curMax:
                res.append(True)
            else:
                res.append(False)
        return res