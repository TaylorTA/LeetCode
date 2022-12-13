class Solution:
    def reverseBits(self, n: int) -> int:
        r = 0
        pos = 31

        while n:
            r += (n&1) << pos
            n >>= 1
            pos -= 1
        
        return r
