class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = collections.defaultdict(list)

        for n1, n2 in edges:
            g[n1].append(n2)
            g[n2].append(n1)

        seen = set()

        def dfs(n):
            if n == destination:
                return True
            if n not in seen:
                seen.add(n)
                for e in g[n]:
                    if dfs(e):
                        return True
            return False
        
        return dfs(source)
