class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = [char for char in str(x)]
        l = 0
        r = len(s)-1
        
        if s[::] == s[::-1]:
            return True
        else:
            return False