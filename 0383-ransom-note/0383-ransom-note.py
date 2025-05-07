class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mMap = Counter(magazine)
        rMap = Counter(ransomNote)
        
        for char in rMap:
            if char not in mMap:
                return False
            elif mMap[char] < rMap[char]:
                return False
        return True