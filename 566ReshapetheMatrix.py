class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat
        
        reshape = [[0]*c for _ in range(r)]
        
        i = 0
        j = 0
        
        for mr in range(len(mat)):
            for mc in range(len(mat[0])):
                reshape[i][j] = mat[mr][mc]
                if j + 1 == c:
                    i +=1
                    j = 0
                else:
                    j +=1
                
        return reshape
