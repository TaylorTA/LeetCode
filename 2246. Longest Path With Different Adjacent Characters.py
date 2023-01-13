class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        tree = [[] for _ in range(len(s))]
        for i in range(1,len(parent)):
            if s[i] != s[parent[i]]:
                tree[i].append(parent[i])
                tree[parent[i]].append(i)
        
        visited = [False] * len(s)
        mp = 0

        def bfs(i):
            q_start = 0
            q = []
            cv = [False] * len(parent)
            d = [-1] * len(parent)
            q.append(i)
            cv[i] = True
            d[i] = 0
            while q_start < len(q):
                cn = q[q_start]
                q_start += 1
                visited[cn] = True
                for adj in tree[cn]:
                    #print(adj)
                    #print(cv)
                    if not cv[adj]:
                        cv[adj] = True
                        d[adj] = d[cn]+1
                        q.append(adj)
            cm = -1
            mi = -1
            for n in range(len(parent)):
                if d[n] > cm:
                    cm = d[n]
                    mi = n
            return cm, mi

        for i in range(len(parent)):
            if visited[i] or len(tree[i])==0:
                continue
            cm, mi = bfs(i)
            cm, _ = bfs(mi)
            #print(i, cm)
            mp = max(mp, cm)
        
        return mp+1
