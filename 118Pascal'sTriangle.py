class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        
        for r in range(numRows):
            row = [1]
            if r > 1:
                for i in range(1, len(triangle[r-1])):
                    row.append(triangle[r-1][i-1]+triangle[r-1][i])
            if r > 0:
                row.append(1)
            triangle.append(row)
        
        return triangle
