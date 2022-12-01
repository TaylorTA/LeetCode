class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        c1 = 0
        c2 = 0

        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                if i < len(s)/2:
                    c1 += 1
                else:
                    c2 += 1

        return c1 == c2
