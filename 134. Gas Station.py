class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        t, s, ct = 0, 0, 0
        for i, (g, c) in enumerate(list(zip(gas, cost))):
            t += (g - c)
            ct += (g - c)
            if ct < 0:
                s = i+1
                ct = 0
            
        return s if t>=0 else -1
