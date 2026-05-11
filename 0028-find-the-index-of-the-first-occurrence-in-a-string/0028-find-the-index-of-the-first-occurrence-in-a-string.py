class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        for i in range(len(haystack)-n+1):
            if haystack[i:n+i] == needle:
                return i
        return -1