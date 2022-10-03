class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        cmax = neededTime[0]
        
        for i in range(1, len(colors)):
            if colors[i] != colors[i-1]:
                cmax = 0
                
            total += min(neededTime[i], cmax)
            cmax = max(neededTime[i], cmax)
        
        return total
