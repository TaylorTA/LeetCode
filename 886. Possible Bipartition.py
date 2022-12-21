class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        g = collections.defaultdict(list)
        for p1, p2 in dislikes:
            g[p1].append(p2)
            g[p2].append(p1)
        group = [-1]*(n+1)

        def dfs(p, c):
            group[p] = c
            for dl in g[p]:
                if group[dl] == group[p]:
                    return False
                elif group[dl] == -1 and not dfs(dl, 1-c):
                    return False
            return True

        for p in range(n+1):
            if group[p] == -1:
                if not dfs(p, 0):
                    return False
        return True
