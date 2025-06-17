class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        
        for i in range(0, len(s)-2):
            summ = 0
            for char in s[i:i+3]:
                summ += s[i:i+3].count(char)
            if summ == 3:
                count += 1
        return count