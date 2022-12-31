class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        nr = len(grid)
        nc = len(grid[0])

        ns, sr, sc, er, ec = 0, 0, 0, 0, 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == 1:
                    sr = r
                    sc = c
                if grid[r][c] == 2:
                    er = r
                    ec = c
                if grid[r][c] != -1:
                    ns += 1
        
        np = 0
        def bk(cr, cc, ps):
            nonlocal np
            #print(ns, ps)
            if grid[cr][cc] == 2 and ps == ns:
                np += 1
                print(np)
                return
            ps += 1
            temp = grid[cr][cc]
            grid[cr][cc] = -1

            for r, c in [(0,1), (0,-1), (1,0), (-1,0)]:
                r, c = cr + r, cc + c
                if 0<=r<nr and 0<=c<nc and grid[r][c] != -1 and abs(r-er) + abs(c-ec) <= ns-ps:
                    bk(r,c,ps)
            
            grid[cr][cc] = temp

        bk(sr, sc, 1)
        return np
            
