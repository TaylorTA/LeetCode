class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        s = 0
        p = 1
        
        for c in n:
            digit = int(c)
            s = s+digit
            p = p*digit
        
        return p - s
