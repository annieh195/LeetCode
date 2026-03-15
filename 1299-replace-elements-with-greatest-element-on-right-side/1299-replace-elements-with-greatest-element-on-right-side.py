class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [0]*len(arr)
        lastMax = -1

        for i in range(len(arr)-1, -1, -1):
            res[i] = lastMax
            lastMax = max(arr[i], lastMax)
        return res