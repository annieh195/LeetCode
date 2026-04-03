class Solution:
    def isValid(self, s: str) -> bool:
        check = []
        mp = {")":"(", "}":"{", "]":"["}
        for char in s:
            if char in mp.values():
                check.append(char)
            elif char in mp.keys():
                if not check or mp[char] != check.pop():
                    return False
        return not check