class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [[] for i in range(numRows)]
        i = 0
        d = False
        for c in s:
            rows[i].append(c)
            if i == 0 or i == numRows-1:
                d = not d
            if d:
                i += 1
            else:
                i -= 1
        return ''.join("".join(r) for r in rows)
