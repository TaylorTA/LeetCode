class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        s = []

        for c in num:
            if c in ['1', '0', '8']:
                s.append(c)
            elif c == '6':
                s.append('9')
            elif c == '9':
                s.append('6')
            else:
                return False
        s.reverse()
        
        return "".join(s) == num
