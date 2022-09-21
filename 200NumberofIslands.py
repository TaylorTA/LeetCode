class Solution:
    def helper(self, grid, r, c):
        if grid[r][c] == "0":
            return
        else:
            grid[r][c] = "0"
            if r-1 >= 0:
                self.helper(grid, r-1, c)
            if r+1 < len(grid):
                self.helper(grid, r+1, c)
            if c-1 >= 0:
                self.helper(grid, r, c-1)
            if c+1 < len(grid[0]):
                self.helper(grid, r, c+1)
                              
        
    def numIslands(self, grid: List[List[str]]) -> int:
        numI = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    numI += 1
                    self.helper(grid, i, j)
        
        return numI
