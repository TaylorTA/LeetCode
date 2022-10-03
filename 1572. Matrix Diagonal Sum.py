class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s = 0
        for i, row in enumerate(mat):
            s += row[i] + row[-(i+1)]
        if len(mat)%2 == 1:
            s -= mat[len(mat)//2][len(mat)//2]
        return s
