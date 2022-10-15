class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache
        def dp(a, b, c, d):
            if b > k:
                return math.inf
            if a == len(s):
                return 0
            
            delete = dp(a+1, b+1, c, d)
            
            if s[a] == c:
                if d == 1 or d == 9 or d == 99:
                    keep = dp(a+1, b, c, d+1) + 1
                else:
                    keep = dp(a+1, b, c, d+1)
            else:
                keep = dp(a+1, b, s[a], 1) + 1
                
            return min(keep, delete)
        
        return dp(0, 0, "", 0)
