class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0

        for each in details:
            if int(each[11:13]) > 60:
                res += 1
        return res