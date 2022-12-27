class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        rs = [capacity[i]-rocks[i] for i in range(len(capacity))]
        rs.sort()
        nb = 0

        for r in rs:
            if r <= additionalRocks:
                additionalRocks -= r
                nb += 1
            else:
                break

        return nb
