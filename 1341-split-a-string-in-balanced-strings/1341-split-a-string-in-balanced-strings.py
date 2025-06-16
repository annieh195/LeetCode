class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        countL = 0
        countR = 0

        for i in range(len(s)):
            if countL == countR and countL >= 1 and countR >= 1:
                res += 1
                countL = 0
                countR = 0
            if s[i] == 'R':
                countR += 1
            if s[i] == 'L':
                countL += 1
        return res+1