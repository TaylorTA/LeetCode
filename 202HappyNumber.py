class Solution:
    def getNext(self, n: int) -> int:
        total = 0
        
        while n>0:
            total += (n%10) ** 2
            n //= 10
        return total
    
        
    def isHappy(self, n: int) -> bool:
        nums = set()
        
        while n!=1 and n not in nums:
            nums.add(n)
            n = self.getNext(n)
        
        return n == 1
