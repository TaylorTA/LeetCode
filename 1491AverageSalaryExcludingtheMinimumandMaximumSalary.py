class Solution:
    def average(self, salary: List[int]) -> float:
        total = 0
        minS = math.inf
        maxS = 0
        
        for s in salary:
            if s < minS:
                minS = s
            if s > maxS:
                maxS = s
            total += s
        
        return (total - minS - maxS)/(len(salary)-2)
