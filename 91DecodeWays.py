class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        
        dp = [0] * (len(s)+1)
        
        dp[-1] = 1
        
        if s[-1] == '0':
            dp[-2] = 0
        else:
            dp[-2] = 1
        
        for i in range(len(s)-2, -1, -1):
            if s[i] != '0':
                dp[i] += dp[i+1]
            n = s[i:i+2]
            if n >= '10' and n <= '26':
                dp[i] += dp[i+2]
        
        return dp[0]
