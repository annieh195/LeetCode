class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def check(ops, num1, num2):
            if ops == '+':
                return num1 + num2
            if ops == '-':
                return num1 - num2
            elif ops == '*':
                return num1 * num2
            elif ops == '/':
                return num1 / num2 if num2 else 0 

        if len(tokens) == 1:
            return int(tokens[0])

        ops = ['+', '-', '*', '/']
        stack = []
        for token in tokens:
            # print(stack)
            if token not in ops:
                stack.append(token)
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                math_res = int(check(token, num1, num2))  
                # print(math_res)
                stack.append(math_res)
        # print(stack)
        res = stack[0]
        return res