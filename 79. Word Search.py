class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        vd = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if r-1 >=0 and (r-1, c) not in vd and board[r-1][c] == word[i]:
                vd.add((r-1,c))
                if dfs(r-1, c, i+1):
                    return True
                vd.remove((r-1, c))
            print(r+1, c)
            if r+1 < len(board) and (r+1, c) not in vd and board[r+1][c] == word[i]:
                vd.add((r+1, c))
                if dfs(r+1, c, i+1):
                    return True
                vd.remove((r+1, c))
            if c-1 >= 0 and (r, c-1) not in vd and board[r][c-1] == word[i]:
                vd.add((r, c-1))
                if dfs(r, c-1, i+1):
                    return True
                vd.remove((r, c-1))
            if c+1 < len(board[0]) and (r, c+1) not in vd and board[r][c+1] == word[i]:
                vd.add((r, c+1))
                if dfs(r, c+1, i+1):
                    return True
                vd.remove((r, c+1))
            return False

        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    vd.add((r,c))
                    if dfs(r, c, 1):
                        return True
                    vd.remove((r,c))
        return False
