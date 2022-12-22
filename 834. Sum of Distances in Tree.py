class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        g = collections.defaultdict(set)
        for n1, n2 in edges:
            g[n1].add(n2)
            g[n2].add(n1)
        ct = [1] * n
        ans = [0] * n

        def ctst(node, parent):
            for c in g[node]:
                if c != parent:
                    ctst(c, node)
                    ct[node] += ct[c]
                    ans[node] += ans[c] + ct[c]
        
        def ga(node, parent):
            for c in g[node]:
                if c != parent:
                    ans[c] = ans[node] - ct[c] + (n - ct[c])
                    ga(c, node)
        
        ctst(0, None)
        ga(0, None)

        return ans
