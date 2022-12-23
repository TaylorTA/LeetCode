class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0]*(len(prices)+2)
        for d in range(len(prices)-1, -1, -1):
            s = 0
            for pd in range(d+1, len(prices)):
                s = max(s, prices[pd]-prices[d]+dp[pd+2])
            dp[d] = max(s, dp[d+1])
        return dp[0]
