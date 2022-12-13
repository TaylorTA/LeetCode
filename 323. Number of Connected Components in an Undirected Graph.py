class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dic = {}
        for e in edges:
            n1 = e[0]
            n2 = e[1]
            if n1 not in dic:
                dic[n1] = [n2]
            else:
                dic[n1].append(n2)
            if n2 not in dic:
                dic[n2] = [n1]
            else:
                dic[n2].append(n1)
        print(dic)
        
        def dp(n):
            vd.add(n)
            if n not in dic:
                return
            for e in dic[n]:
                if e not in vd:
                    dp(e)
    
        c = 0
        vd = set()
        for n in range(0,n):
            if n not in vd:
                dp(n)
                c+= 1
        
        return c
            
