class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        profit = 0
        minP = prices[0]

        for cp in prices:
            if cp < minP:
                minP = cp
            
            profit = max(cp - minP, profit)
        
        return profit
