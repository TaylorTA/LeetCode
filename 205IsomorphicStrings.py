class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sToT = {}
        tToS = {}
        for i in range(len(s)):
            if (s[i] not in sToT) and (t[i] not in tToS):
                sToT[s[i]] = t[i]
                tToS[t[i]] = s[i]
            
            if sToT.get(s[i]) != t[i] or tToS.get(t[i]) != s[i]:
                return False
        
        return True
