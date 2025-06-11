class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp1 = {}
        mp2 = {}

        for i in range(len(s)):
            if s[i] not in mp1:
                mp1[s[i]] = i
            if t[i] not in mp2:
                mp2[t[i]] = i
            if mp1[s[i]] != mp2[t[i]]:
                return False
        return True

        

