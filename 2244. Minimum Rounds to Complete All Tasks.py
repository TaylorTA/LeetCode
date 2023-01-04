class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        c = Counter(tasks)
        d = 0

        for t in c:
            if c[t] == 1:
                return -1
            elif c[t]%3 != 0:
                d += 1
            d += c[t]//3

        return d
