class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        newS = s.split()
        return len(newS[-1])