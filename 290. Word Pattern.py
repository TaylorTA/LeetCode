class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        tokens = s.split()
        if len(pattern) != len(tokens):
            return False
        d = {}
        seen = set()
        for n, c in enumerate(pattern):
            if c not in d:
                if tokens[n] not in seen:
                    d[c] = tokens[n]
                    seen.add(tokens[n])
                else:
                    return False
            elif d[c] != tokens[n]:
                return False
        return True
