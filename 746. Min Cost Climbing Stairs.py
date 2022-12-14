class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost)+1)
        dp[-2] = cost[-1]

        for i in range(len(cost)-2, -1, -1):
            #print(dp)
            dp[i] = min(cost[i]+dp[i+1], cost[i]+dp[i+2])
        return min(dp[1], dp[0])
