class Solution:
    def numSquares(self, n: int) -> int:
        s = [i**2 for i in range(int(math.sqrt(n))+1)]

        level = 0
        q = [n]

        while q:
            level += 1

            nextq = []
            for r in q:
                for rt in s:
                    if r == rt:
                        return level
                    elif r > rt:
                        nextq.append(r-rt)
            q = nextq

        return level
