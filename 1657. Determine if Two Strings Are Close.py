class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)

        return Counter(c1.values()) == Counter(c2.values()) and Counter(c1.keys()) == Counter(c2.keys())
