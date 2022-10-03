class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        uneq = []
        
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if len(uneq) == 2:
                    return False
                else:
                    uneq.append(i)
                
        if len(uneq) == 0:
            return True
        
        if len(uneq) == 2 and s1[uneq[0]] == s2[uneq[1]] and s1[uneq[1]] == s2[uneq[0]]:
            return True
        else:
            return False
