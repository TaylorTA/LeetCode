class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # 01010
        ones = 0
        flip = 0
        for c in s:
            if c == '0':
                flip = min(ones, flip+1)
            else:
                ones += 1
        return flip
