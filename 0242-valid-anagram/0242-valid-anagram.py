class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp1 = defaultdict(int)
        mp2 = defaultdict(int)

        if len(s) != len(t):
            return False
        
        for char in s:
            mp1[char] += 1

        for char in t:
            mp2[char] += 1
        
        for char in s:
            if mp1[char] != mp2[char]:
                return False
        return True