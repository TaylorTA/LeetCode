class Solution:
    def numTilings(self, n: int) -> int:
        if n<2:
            return n
        dp = [0] * (n+1)
        nf = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        nf[2] = 1

        for i in range(3, n+1):
            dp[i] = dp[i-1]+dp[i-2]+2*nf[i-1]
            nf[i] = nf[i-1] + dp[i-2]
        
        return dp[n]%(10**9+7)
