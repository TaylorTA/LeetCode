class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted([(t[0],t[1],i) for i, t in enumerate(tasks)])
        c = 0
        d = []
        h = []
        t = tasks[0][0]

        while len(d) < len(tasks):
            while c<len(tasks) and tasks[c][0] <= t:
                heapq.heappush(h, (tasks[c][1],tasks[c][2]))
                c += 1
            if h:
                ct, i = heapq.heappop(h)
                t += ct
                d.append(i)
            elif c < len(tasks):
                t = tasks[c][0]
        
        return d
