class Solution:
    def firstUniqChar(self, s: str) -> int:
        mp = defaultdict(int)

        for char in s:
            mp[char] += 1
        
        for i in range(len(s)):
            if mp[s[i]] == 1:
                return i
        return -1
            