class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        dic = collections.defaultdict(list)
        for t1, t2 in trust:
            dic[t1].append(t2)
        
        for p in range(1, n+1):
            # print(p)
            # print(dic[p])
            if not dic[p]:
                nt = 0
                for tp in range(1, n+1):
                    if tp != p and p in dic[tp]:
                        nt += 1
                #print(p,nt)
                if nt == n-1:
                    return p
        return -1
