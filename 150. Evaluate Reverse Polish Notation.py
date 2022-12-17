class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for n in tokens:
            if n not in '+-*/':
                stack.append(int(n))
            else:
                n1 = stack.pop()
                n2 = stack.pop()
                if n == '+':
                    n1 = n1 + n2
                elif n == '-':
                    n1 = n2 - n1
                elif n == '*':
                    n1 = n1 * n2
                else:
                    n1 = int(n2/n1)
                stack.append(n1)
        return stack.pop()
