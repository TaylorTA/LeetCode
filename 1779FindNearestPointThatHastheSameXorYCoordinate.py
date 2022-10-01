class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        index = -1
        mind = math.inf
        
        for i in range(len(points)):
            px = points[i][0]
            py = points[i][1]
            
            if px == x:
                d = abs(py-y)
                if d < mind:
                    mind = d
                    index = i
            if py == y:
                d = abs(px-x)
                if d < mind:
                    mind = d
                    index = i
        
        return index
