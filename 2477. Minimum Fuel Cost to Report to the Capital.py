class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        global fuel
        fuel = 0

        g = collections.defaultdict(list)
        for a,b in roads:
            g[a].append(b)
            g[b].append(a)
        
        def dfs(cur, pre):
            global fuel
            rep = 1
            for n in g[cur]:
                if n != pre:
                    rep += dfs(n, cur)
            if cur != 0:
                fuel += math.ceil(rep/seats)
            return rep
        
        dfs(0,-1)
        return fuel
