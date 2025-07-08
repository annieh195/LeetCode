class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def check_math(op, num1, num2):
            if op == '+':
                return num1 + num2
            elif op == '-':
                return num1 - num2
            elif op == '*':
                return num1 * num2
            else:
                return num1 / num2 if num2 else 0
        
        if len(tokens) == 1:
            return int(tokens[0])
        
        ops = ['+', '-', '*', '/']
        stack = []
        ans = 0

        for token in tokens:
            if token not in ops:
                stack.append(token)
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                ans = int(check_math(token, num1, num2))
                stack.append(ans)
        return stack[0]