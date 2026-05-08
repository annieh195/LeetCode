class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        inc = ["++X", "X++"]
        res = 0
        for op in operations:
            if op in inc:
                res += 1
            else:
                res -= 1
        return res
