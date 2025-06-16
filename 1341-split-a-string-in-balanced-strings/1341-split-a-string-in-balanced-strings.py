class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        countL = 0
        countR = 0

        for i in range(len(s)):
            if s[i] == 'R':
                countR += 1
            if s[i] == 'L':
                countL += 1
            if countL == countR:
                res += 1
        return res