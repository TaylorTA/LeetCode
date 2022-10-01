class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = [0] * 26
        nchar = 0
        
        for c in word:
            if freq[ord(c) - ord('a')] == 0:
                nchar += 1
            freq[ord(c) - ord('a')] += 1
            
        freq = list(filter(lambda num: num != 0, freq))
            
        for i in range(len(freq)):
            freq[i] -= 1
            uniques = {}
            for x in freq:
                if x > 0:
                    uniques[x] = True
            if len(uniques) == 1:
                return True
            freq[i] += 1
        
        
        return False
