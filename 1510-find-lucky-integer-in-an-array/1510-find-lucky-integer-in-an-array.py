class Solution:
    def findLucky(self, arr: List[int]) -> int:
        maxx = -1
        for num in arr:
            if num == arr.count(num):
                maxx = max(maxx, num)
        return maxx