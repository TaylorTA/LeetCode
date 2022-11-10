class Solution:
    def removeDuplicates(self, s: str) -> str:
        s = list(s)

        c = 0
        n = 1

        while(n<len(s)):
            if s[c] == s[n]:
                del s[n]
                del s[c]
                if c > 0:
                    c -= 1
                    n -= 1
            else:
                c += 1
                n += 1
        
        return "".join(s)
