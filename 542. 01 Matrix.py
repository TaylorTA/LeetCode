class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        d = [[math.inf]*n for _ in range(m)]
        q = deque()
        dirc = [(1,0), (-1,0), (0,1), (0,-1)]

        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    d[r][c] = 0
                    q.append((r,c))
        
        while q:
            cr, cc = q.popleft()
            for dr, dc in dirc:
                nr, nc = cr+dr, cc+dc
                
                if nr >= 0 and nr < m and nc >= 0 and nc < n:
                    if d[nr][nc] > d[cr][cc] + 1:
                        d[nr][nc] = d[cr][cc] + 1
                        q.append((nr,nc))
        
        return d
