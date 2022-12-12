class Solution:
    def hammingWeight(self, n: int) -> int:
        s = 0
        while n!=0:
            if n & 1 == 1:
                s += 1
            n >>= 1
        return s
