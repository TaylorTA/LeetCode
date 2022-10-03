class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        op = 0
        for i in range(2, len(grid)):
            for j in range(2, len(grid[0])):
                op = max(op, grid[i-2][j-2] + grid[i-2][j-1] + grid[i-2][j] + grid[i-1][j-1] + grid[i][j-2] + grid[i][j-1] + grid[i][j])
        
        return op
