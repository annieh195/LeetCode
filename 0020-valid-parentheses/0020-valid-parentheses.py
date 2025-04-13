class Solution:
    def isValid(self, s: str) -> bool:
        check = []
        mapParentheses = {")":"(", "}":"{", "]":"["}
        for char in s:
            if char in mapParentheses.values():
                check.append(char)
            elif char in mapParentheses.keys():
                if not check or mapParentheses[char] != check.pop():
                    return False
        return not check