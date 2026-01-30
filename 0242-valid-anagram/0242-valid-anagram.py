class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mp1 = defaultdict(int)
        mp2 = defaultdict(int)

        for charS, charT in zip(s, t):
            mp1[charS] += 1
            mp2[charT] += 1
        
        return mp1 == mp2