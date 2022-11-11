class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        blocks = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == '.':
                    continue
                else:
                    if v in rows[r]:
                        return False
                    rows[r].add(v)

                    if v in cols[c]:
                        return False
                    cols[c].add(v)

                    b = r//3 * 3 + c//3
                    if v in blocks[b]:
                        return False
                    blocks[b].add(v)
        
        return True
