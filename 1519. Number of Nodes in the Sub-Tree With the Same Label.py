class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        tree = collections.defaultdict(list)
        for e in edges:
            tree[e[0]].append(e[1])
            tree[e[1]].append(e[0])

        l = [[0]*26 for _ in range(len(labels))]
        q = []
        for i in range(n):
            l[i][ord(labels[i])-ord('a')] = 1
            if len(tree[i]) == 1 and i != 0:
                q.append(i)
        #print(q)

        while(q):
            cur = q[0]
            #print(cur)
            #print(tree[cur])
            p = tree[cur][0]
            tree[p].remove(cur)
            for i in range(26):
                l[p][i] += l[cur][i]
            if len(tree[p]) == 1 and p != 0:
                q.append(p)
            q.pop(0)
        
        ans = [0] * n
        for i in range(n):
            ans[i] = l[i][ord(labels[i]) - ord('a')]
        
        return ans
