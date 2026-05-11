class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for x in s:
            if x.isalnum():
                res += x.lower()
        return (res) == res[::-1]