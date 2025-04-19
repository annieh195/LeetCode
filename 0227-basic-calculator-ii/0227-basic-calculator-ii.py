class Solution:
    def calculate(self, s: str) -> int:
        s = ''.join(s.split())
        stack = []
        i = 0
        j = 0

        def get_num(i):
            j = i + 1
            a = 0
            while j < len(s) and s[j].isdigit():
                j += 1
            stack.append(int(s[i:j]))
            return j

        while i < len(s):
            if s[i] == '+':
                i += 1
                continue 
            if s[i].isdigit() or s[i] == '-':
                i = get_num(i)
            else:
                j = get_num(i+1)
                num1, num2 = stack.pop(), stack.pop()
                if s[i] == "*":
                    stack.append(num2*num1)
                elif s[i] == "/":
                    # print(num2, num1, num2/num1)
                    a = abs(num2)//abs(num1)
                    if num2/num1 < 0:
                        a *= -1
                    stack.append(a)
                    # print(stack)
                i = j
      
        return int(sum(stack))