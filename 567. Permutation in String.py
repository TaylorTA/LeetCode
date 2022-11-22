class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        s1c = Counter(s1)
        s2c = Counter()

        for i in range(len(s1)):
            s2c[s2[i]] += 1
        
        l = 0
        for i in range(len(s1), len(s2)):
            if s1c == s2c:
                return True
            s2c[s2[i]] += 1
            s2c[s2[l]] -= 1
            if s2c[s2[l]] == 0:
                s2c.pop(s2[l])
            l += 1

        return s1c == s2c
