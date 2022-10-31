class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return True
        
        for i in range(len(matrix)):
            n = matrix[i][0]
            for j in range(1, len(matrix[0])):
                if i+j < len(matrix) and matrix[i+j][j] != n:
                    return False
        
        for j in range(len(matrix[0])):
            n = matrix[0][j]
            for i in range(1, len(matrix)):
                if i+j < len(matrix[0]) and matrix[i][i+j] != n:
                    return False
        
        return True
