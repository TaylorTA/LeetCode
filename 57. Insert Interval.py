class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        pos = bisect_right([i[0] for i in intervals], newInterval[0])
        intervals.insert(pos, newInterval)

        ans = []
        cs, ce = intervals[0]
        for s, e in intervals:
            if s > ce:
                ans.append([cs,ce])
                cs = s
                ce = e
            elif e > ce:
                ce = e
        ans.append([cs,ce])
        
        return ans
