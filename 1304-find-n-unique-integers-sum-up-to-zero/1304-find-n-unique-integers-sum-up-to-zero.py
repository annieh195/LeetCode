class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        x = 1
        for i in range(n // 2):
            res.append(x)
            res.append(-x)
            x += 1
        if n % 2 == 0:
            return res
        res.append(0)
        return res