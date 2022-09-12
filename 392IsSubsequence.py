class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        currS = 0
        currT = 0
        
        if len(s) == 0:
            return True
        
        while currT < len(t) and currS < len(s):
            if s[currS] == t[currT]:
                currS += 1
                if currS == len(s):
                    return True
            currT += 1
        
        return False
