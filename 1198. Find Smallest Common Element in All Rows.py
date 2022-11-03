class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        
        for c in range(n):
            num = mat[0][c]
            for r in range(m):
                if num not in mat[r]:
                    break
                if num in mat[r] and r == m-1:
                    return num
        
        return -1
