class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for s, e in redEdges:
            graph[s].append((e,0))
        for s, e in blueEdges:
            graph[s].append((e,1))
        
        ans = [math.inf] * n
        vd = set()
        d = 0
        q = collections.deque([(0,0),(0,1)])

        while q:
            for _ in range(len(q)):
                cn, cc = q.popleft()
                ans[cn] = min(ans[cn], d)
                for nn, nc in graph[cn]:
                    if nc!= cc and (nn,nc) not in vd:
                        vd.add((nn,nc))
                        q.append((nn,nc))
            d += 1
        
        for i in range(n):
            ans[i] = -1 if ans[i] == math.inf else ans[i]

        return ans
