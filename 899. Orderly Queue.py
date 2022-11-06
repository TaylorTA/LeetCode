class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            possibles = []
            for i, c in enumerate(s):
                possibles.append(s[i:] + s[:i])
            return min(possibles)
        return "".join(sorted(s))
