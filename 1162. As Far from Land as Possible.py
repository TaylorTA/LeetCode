class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = collections.deque()

        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    q.append((r,c))
        
        d = -1
        vd = set()
        if len(q) == m*n:
            return d
            
        while q:
            for _ in range(len(q)):
                cr, cc = q.popleft()
                
                for dr, dc in ((-1,0), (1,0), (0,1), (0,-1)):
                    nr, nc = cr+dr, cc+dc
                    if 0<=nr<m and 0<=nc<n and not grid[nr][nc] and (nr,nc) not in vd:
                        vd.add((nr,nc))
                        q.append((nr,nc))
            d += 1
        return d
