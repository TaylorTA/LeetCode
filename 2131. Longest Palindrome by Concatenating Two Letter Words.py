class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ct = Counter(words)
        maxl = 0
        
        for word in words:
            if word != word[::-1] and word[::-1] in ct and ct[word[::-1]] > 0 and ct[word] > 0:
                maxl += 4
                ct[word] -= 1
                ct[word[::-1]] -= 1
            elif word == word[::-1] and ct[word] > 1:
                ct[word] -= 2
                maxl += 4
            # print(word)
            # print(ct)
            # print(maxl)
        
        for word in words:
            if word[0] == word[1] and ct[word] == 1:
                maxl += 2
                break
        
        return maxl
