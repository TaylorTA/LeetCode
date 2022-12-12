class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        p = triangle[-1]
        for r in range(len(triangle)-2, -1, -1):
            c = []
            for i in range(len(p)-1):
                c.append(min(p[i], p[i+1])+triangle[r][i])
            p = c
        return p[0]
