class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxa = 0
        m = len(grid)
        n = len(grid[0])
        visited = set()

        def dfs(r, c, a):
            a += 1
            visited.add((r,c))
            if r-1 >= 0 and (r-1, c) not in visited and grid[r-1][c] == 1:
                a = dfs(r-1, c, a)
            if r+1 < m and (r+1, c) not in visited and grid[r+1][c] == 1:
                a = dfs(r+1, c, a)
            if c-1 >= 0 and (r, c-1) not in visited and grid[r][c-1] == 1:
                a = dfs(r, c-1, a)
            if c+1 < n and (r, c+1) not in visited and grid[r][c+1] == 1:
                a = dfs(r, c+1, a)
            return a
        
        for r in range(m):
            for c in range(n):
                if (r, c) not in visited and grid[r][c] == 1:
                    a = dfs(r, c, 0)
                    #print(r, c, a)
                    maxa = max(maxa, a)
        
        return maxa
