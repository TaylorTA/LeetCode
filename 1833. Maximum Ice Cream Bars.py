class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        i = 0
        for c in costs:
            if c <= coins:
                coins -= c
                i += 1
            else:
                break
        return i
