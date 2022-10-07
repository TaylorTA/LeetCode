class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic = defaultdict(int)
        
        for c in s:
            dic[c] += 1
        
        for c in t:
            if c not in dic:
                return c
            else:
                dic[c] -= 1
                if dic[c] == 0:
                    dic.pop(c)
        
        return dic[0]
