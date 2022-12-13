class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def bk(s, cur):
            if len(cur) == k:
                op.append(cur[:])
            for i in range(s, n+1):
                cur.append(i)
                bk(i+1, cur)
                cur.pop()
        
        op = []
        bk(1, [])
        return op
