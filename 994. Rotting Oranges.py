class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        m = len(grid)
        n = len(grid[0])
        nfo = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        l = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    nfo += 1
        
        q.append((-1,-1))
        while q:
            r, c = q.popleft()
            if r == -1:
                if q:
                    l += 1
                    q.append((-1,-1))
            else:
                for d in dirs:
                    nr, nc = r+d[0], c+d[1]
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        nfo -=1
                        q.append((nr, nc))
        
        return l if not nfo else -1
