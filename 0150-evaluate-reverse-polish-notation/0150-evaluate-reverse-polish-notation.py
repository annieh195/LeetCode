class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def calculation(ops, num1, num2):
            if ops == '+':
                return num1+num2
            elif ops == '-':
                return num1-num2
            elif ops == '*':
                return num1*num2
            else:
                return int(num1 / num2)

        stack = []
        ops = ['+', '-', '*', '/']
        for i in range(len(tokens)):
            if tokens[i] in ops:
                num2 = stack.pop()
                num1 = stack.pop()
                ans = calculation(tokens[i], num1, num2)
                stack.append(ans)
            else:
                stack.append(int(tokens[i]))
        return stack[-1]