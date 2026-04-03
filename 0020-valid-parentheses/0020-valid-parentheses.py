class Solution:
    def isValid(self, s: str) -> bool:
        openBrackets = ['(', '[', '{']
        stack = []

        if len(s) < 2:
            return False

        for char in s:
            if char in openBrackets:
                stack.append(char)
            elif stack and ((stack[-1] == '(' and char == ')') or (stack[-1] == '[' and char == ']') or (stack[-1] == '{' and char == '}')):
                stack.pop()
        
        if stack:
            return False
        else:
            return True