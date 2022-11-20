class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")[::-1]
        stack = []
        num = 0
        dig = 0

        for c in s:
            if c.isdigit():
                num = 10**dig*int(c) + num
                dig += 1

            else:
                if dig:
                    stack.append(num)
                    num = 0
                    dig = 0

                if c == '(' :
                    if stack and type(stack[-1]) is int:
                        n = stack.pop()
                    else:
                        n = 0
                
                    while stack and stack[-1] != ')':
                        sign = stack.pop()
                        if sign == '+':
                            n += stack.pop()
                        else:
                            n -= stack.pop()
                    stack.pop()

                    stack.append(n)
                else:
                    stack.append(c)   

        if dig:
            stack.append(num)

        if stack:
            if stack and type(stack[-1]) is int:
                n = stack.pop()
            else:
                n = 0
            while stack:
                sign = stack.pop()
                if sign == '+':
                    n += stack.pop()
                else:
                    n -= stack.pop()
            stack.append(n)
        

        return stack.pop()
