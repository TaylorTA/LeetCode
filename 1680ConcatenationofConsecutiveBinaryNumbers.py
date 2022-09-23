class Solution:
    def concatenatedBinary(self, n: int) -> int:
        op = 0
        mod = 10**9 + 7
        
        for i in range(1, n+1):
            op = ((op << int(log(i,2)+1)) + i) % mod
        
        return op 
