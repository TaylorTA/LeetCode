class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1 = coordinates[0][0]
        x2 = coordinates[1][0]
        y1 = coordinates[0][1]
        y2 = coordinates[1][1]
        dx = x2 - x1
        dy = y2 - y1
        
        for i in range(1, len(coordinates)):
            x2 = coordinates[i][0]
            y2 = coordinates[i][1]
            
            if dx * (y2-y1) != dy * (x2 - x1):
                return False
        
        return True
