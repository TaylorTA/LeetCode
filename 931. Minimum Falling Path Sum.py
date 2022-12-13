class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for r in range(1,len(matrix)):
            for c in range(len(matrix[0])):
                m = matrix[r-1][c]
                if c > 0:
                    m = min(m, matrix[r-1][c-1])
                if c < len(matrix[0])-1:
                    m = min(m, matrix[r-1][c+1])
                matrix[r][c] += m
        return min(matrix[-1])
