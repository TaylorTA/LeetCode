class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        curp = 0
        t = 0
        sort = sorted(zip(growTime, plantTime))
        for g, p in reversed(sort):
            curp += p
            t = max(t, curp+g)
        
        return t
