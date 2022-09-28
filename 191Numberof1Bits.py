class Solution:
    def hammingWeight(self, n: int) -> int:
        mask = 1
        num1 = 0
        
        for i in range(32):
            if n & mask:
                num1 += 1
            mask = mask<<1
        
        return num1
