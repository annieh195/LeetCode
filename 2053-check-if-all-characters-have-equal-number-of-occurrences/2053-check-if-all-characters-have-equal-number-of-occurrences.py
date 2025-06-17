class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        mp = defaultdict(int)

        for char in s:
            mp[char] += 1

        if len(set(mp.values())) == 1:
            return True
        return False