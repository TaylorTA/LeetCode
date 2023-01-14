class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        dic = {}
        for i in range(26):
            c = chr(i+ord('a'))
            dic[c] = c
        
        def s(c): 
            while(c!=dic[c]):
                c = dic[c]
            return c
        
        def reduce(c1, c2):
            c1 = s(c1)
            c2 = s(c2)
            if c1 == c2:
                return
            elif c1 > c2:
                dic[c1] = c2
            else:
                dic[c2] = c1
            return
        
        for i in range(len(s1)):
            reduce(s1[i], s2[i])
        
        ans = []
        for i in range(len(baseStr)):
            ans.append(s(baseStr[i]))
        return "".join(ans)
