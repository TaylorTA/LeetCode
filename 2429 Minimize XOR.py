class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        n2 = bin(num2).count("1")
        n1 = bin(num1).count("1")
        op = 0
        
        if n1 == n2:
            return num1
        if n1 < n2:
            mask = 1
            remain = n2 - n1
            while remain > 0:
                if mask & num1 == 0:
                    num1 = num1 | mask
                    remain -= 1
                mask = mask << 1
            return num1
        else:
            mask = 1
            remain = n1 - n2
            while remain>0:
                if (mask & num1) >= 1:
                    num1 = num1 ^ mask
                    remain -= 1
                mask = mask << 1
            return num1
