class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        s = s.lower()
        def bk(f, cur):
            if f == len(s):
                op.append("".join(cur))
                return
            if s[f].isalpha():
                cur.append(s[f])
                bk(f+1, cur)
                cur.pop()
                cur.append(s[f].upper())
                bk(f+1, cur)
                cur.pop()
            else:
                cur.append(s[f])
                bk(f+1, cur)
                cur.pop()
        op = []
        bk(0,[])
        return op
