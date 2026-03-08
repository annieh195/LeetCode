class Solution:
    def scoreOfString(self, s: str) -> int:
        l = 0
        r = l+1
        res = 0

        if len(s) < 2:
            return res

        while r != len(s):
            res += abs(ord(s[l])-ord(s[r]))
            l += 1
            r = l+1
        return res