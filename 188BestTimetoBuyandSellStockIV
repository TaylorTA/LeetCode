class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        d = len(prices)
        # To make a d x k x 2 array:
        matrix = [[[0] * 2 for x in range(k + 1)] for y in range(d)]
        matrix[0][0][0] = 0
        
        for j in range(k + 1):
            matrix[0][j][1] = 0 - prices[0]
        
        for i in range(1,d):
            matrix[i][0][0] = matrix[i-1][0][0]
            matrix[i][0][1] = max(matrix[i-1][0][0] - prices[i], matrix[i-1][0][1])
                
            for j in range(1, k+1):
                matrix[i][j][0] = max(matrix[i-1][j][0], matrix[i-1][j-1][1]+prices[i])
                matrix[i][j][1] = max(matrix[i-1][j][0] - prices[i], matrix[i-1][j][1])
        
        # for day in range(d):
        #     print(day, matrix[day])
        
        return max(d0 for d1 in matrix[d - 1] for d0 in d1)
        
