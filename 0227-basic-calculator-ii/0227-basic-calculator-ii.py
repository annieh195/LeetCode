class Solution:
    def calculate(self, s: str) -> int:
        def check(op, stack, cur):
            if op == '-':
                return stack.append(-cur)
            elif op == '+':
                return stack.append(cur)
            elif op == '*':
                return stack.append(stack.pop() * cur)
            elif op == '/':
                return stack.append(int(stack.pop() / cur))
            
        stack = []
        op = "+"
        cur = 0

        for char in s + '+':
            if char == " ":
                continue
            elif char.isdigit():
                cur = (cur * 10) + int(char)
            else:
                check(op, stack, cur)
                cur = 0 
                op = char
        return sum(stack)