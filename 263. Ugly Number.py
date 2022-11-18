class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        def helper(num, d):
            while num%d == 0:
                num = num//d
            return num

        for d in [2, 3, 5]:
            n = helper(n, d)
        return n == 1
