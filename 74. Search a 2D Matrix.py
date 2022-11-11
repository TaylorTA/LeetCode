class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = [matrix[i][0] for i in range(len(matrix))]
        r = max(bisect_right(row, target) - 1, 0)
        c = bisect.bisect_left(matrix[r], target)

        return c < len(matrix[0]) and matrix[r][c] == target
