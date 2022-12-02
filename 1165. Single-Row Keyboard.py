class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        d = {}

        for i,c in enumerate(keyboard):
            d[c] = i
        
        s = 0
        t = 0

        for c in word:
            t += abs(d[c] - s)
            s = d[c]
        
        return t
