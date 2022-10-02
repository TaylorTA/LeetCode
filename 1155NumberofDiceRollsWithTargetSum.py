class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0] * (target+1) for _ in range(n+1)]
        
        dp[n][target] = 1
        
        for i in range(n-1, -1, -1):
            for j in range(target-1, -1, -1):
                ways = 0
                # print(dp)
                # print(i+1)
                # print(j+1)
                for l in range(1, min(k,target - j)+1):
                    # print(l)
                    ways += dp[i+1][j+l]
                    
                dp[i][j] = ways
        
        return dp[0][0] % (10**9 + 7)
