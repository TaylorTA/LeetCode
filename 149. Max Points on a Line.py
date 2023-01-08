class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        m = 2
        for i in range(len(points)):
            d = collections.defaultdict(int)
            for j in range(len(points)):
                if i != j:
                    d[math.atan2(points[i][0]-points[j][0], points[i][1]-points[j][1])] +=1
            m = max(m, max(d.values())+1)
        return m
