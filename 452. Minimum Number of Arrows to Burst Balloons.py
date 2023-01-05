class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = 0
        e = -math.inf
        points.sort(key = lambda x : x[1])

        for p in points:
            if p[0] > e:
                n += 1
                e = p[1]
        
        return n
