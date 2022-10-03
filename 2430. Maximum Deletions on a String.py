class Solution:
    def deleteString(self, s: str) -> int:
        dp = [0] * (len(s)+1)
        maxWay = 1
        
        dp[-1] = 1
        
        for i in range(len(s)-1, -1, -1):
            currMax = 1
            
            for j in range(i+1, len(s)):
                if 2 * j - i > len(s):
                    break
                # print(j)
                # print(s[i:j])
                # print(s[j:j+(j-i)])
                if s[i:j] == s[j:j+(j-i)]:
                    currMax = max(currMax, dp[j] + 1)
            dp[i] = currMax
        
        return dp[0]
