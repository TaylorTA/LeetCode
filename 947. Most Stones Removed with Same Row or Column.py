class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        e = [[] for _ in stones]

        for i in range(len(stones)):
            for j in range(i+1, len(stones)):
                if stones[i][1] == stones[j][1] or stones[i][0] == stones[j][0]:
                    e[i].append(j)
                    e[j].append(i)
        
        vd = [0] * len(stones)
        ng = 0

        def dfs(i):
            vd[i] = 1
            for s in e[i]:
                if vd[s] == 0:
                    dfs(s)
        
        for i, s in enumerate(stones):
            if vd[i] == 0:
                ng += 1
                dfs(i)
        
        return len(stones) - ng
    
