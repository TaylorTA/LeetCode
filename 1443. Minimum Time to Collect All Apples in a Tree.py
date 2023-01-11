class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        g = collections.defaultdict(list)
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        
        def dfs(cur, pre):
            if cur not in g:
                return 0
            t = 0
            for n in g[cur]:
                if n != pre:
                    c = dfs(n, cur)
                    if c>0 or hasApple[n]:
                        t += c + 2
            return t

        return dfs(0, -1) 
