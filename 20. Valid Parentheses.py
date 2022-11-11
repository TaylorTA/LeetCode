class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                le = stack.pop()
                if c == ')' and le != '(':
                    return False
                elif c == '}' and le != '{':
                    return False
                elif c == ']' and le != '[':
                    return False
        
        return len(stack) == 0
