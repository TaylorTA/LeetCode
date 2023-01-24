Select tags
0/5
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        jump = [-1] *(n*n + 1)
        col = list(range(0,n))
        cur = 1
        for row in range(n-1, -1, -1):
            for c in col:
                if board[row][c] != -1:
                    jump[cur] = board[row][c]
                cur += 1
            col.reverse()
        
        steps = [-1]*(n*n+1)
        steps[1] = 0
        q = collections.deque([1])
        while(q):
            cur = q.popleft()
            for nt in range(cur+1, min(cur+6, n*n)+1):
                des = nt
                if jump[nt] != -1:
                    des = jump[nt]
                if steps[des] == -1:
                    steps[des] = steps[cur]+1
                    q.append(des)
        return steps[n*n+1-1]
