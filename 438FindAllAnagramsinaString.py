from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        pchar = Counter(p)
        schar = Counter()
        op = []
        
        for i in range(len(s)):
            schar[s[i]] += 1
            
            if i >= len(p):
                if schar[s[i-len(p)]] == 1:
                   schar.pop(s[i-len(p)]) 
                else:
                    schar[s[i-len(p)]] -= 1
            
            if schar == pchar:
                op.append(i-len(p)+1)
        
        return op
