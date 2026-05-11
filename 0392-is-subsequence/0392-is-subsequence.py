class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        id1 = 0
        id2 = 0

        while id1 < len(s) and id2 < len(t):
            if s[id1] == t[id2]:
                id1 += 1
            id2 += 1
        return id1 == len(s)