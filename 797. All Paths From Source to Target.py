class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []

        def bk(cur, path):
            if cur == (len(graph)-1):
                ans.append(list(path))
                return
            else:
                for n in graph[cur]:
                    path.append(n)
                    bk(n, path)
                    path.pop()

        bk(0, [0])
        return ans
