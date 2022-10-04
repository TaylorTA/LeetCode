class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        m = len(picture)
        n = len(picture[0])
        row = [0] * m
        col = [0] * n
        b = 0
        
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    row[i] += 1
                    col[j] += 1
        
        for i in range(m):
            for j in range(n):
                if row[i] == col[j] and row[i] == 1 and picture[i][j] == 'B':
                    b += 1
        
        return b
