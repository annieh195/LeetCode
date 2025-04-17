class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        close = "("
        openn = ")"
        stack = []

        for char in s:
            if stack and char == ")" and char != stack[-1]:
                stack.pop() 
            else:
                stack.append(char)

        return len(stack)