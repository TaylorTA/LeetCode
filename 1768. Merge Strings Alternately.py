class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        o = ""
        
        for i in range(min(len(word1), len(word2))):
            o += word1[i] + word2[i]
            
        if len(word1) < len(word2):
            o += word2[len(word1):]
        else:
            o += word1[len(word2):]
        
        return o
