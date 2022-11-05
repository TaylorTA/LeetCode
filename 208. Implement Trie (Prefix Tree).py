class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}

        for word in words:
            node = trie
            for c in word:
                node = node.setdefault(c, {})
            node["$"] = word

        hasw = []

        def backtrack(r, c, n):
            l = board[r][c]
            curr = n[l]

            matchw = curr.pop("$", False)

            if matchw:
                hasw.append(matchw)
            
            board[r][c] = "@"

            if r - 1 >= 0 and board[r-1][c] in curr:
                backtrack(r-1, c, curr)
            if c - 1 >= 0 and board[r][c-1] in curr:
                backtrack(r, c-1, curr)
            if r + 1 < len(board) and board[r+1][c] in curr:
                backtrack(r+1, c, curr)
            if c + 1 < len(board[0]) and board[r][c+1] in curr:
                backtrack(r, c+1, curr)
            
            board[r][c] = l
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] in trie:
                    backtrack(r, c, trie)
        
        return hasw
