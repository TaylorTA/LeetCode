class Solution:
    def countOdds(self, low: int, high: int) -> int:
        between = high - low + 1
        
        if high%2 == 1 and low%2 == 1:
            return int(between/2) + 1
    
        return int(between/2)
