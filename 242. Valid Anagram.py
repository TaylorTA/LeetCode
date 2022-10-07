class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dic = defaultdict(int)
        for c in s:
            dic[c] += 1
        
        for c in t:
            if c not in dic:
                return False
            dic[c] -= 1
            if dic[c] == 0:
                dic.pop(c)
        
        return dic == {}
