class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        @cache
        def isP(i1, i2):
            return s[i1]==s[i2] and (i2-i1<=2 or isP(i1+1,i2-1))
        def bt(pos, cur):
            if pos >= len(s):
                ans.append(list(cur))       
            for i in range(pos+1, len(s)+1):
                if isP(pos,i-1):
                    cur.append(s[pos:i])
                    bt(i, cur)
                    cur.pop()
        bt(0,[])
        return ans
