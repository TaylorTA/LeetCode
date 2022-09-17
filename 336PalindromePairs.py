class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        wordDic = {word: i for i, word in enumerate(words)}
        pairs = []
        
        for i, word in enumerate(words):
            # word + rWord
            rWord = word[::-1]
            if rWord in wordDic and i != wordDic[rWord]:
                pairs.append([i, wordDic[rWord]])
            
            # word + first + last
            last = []
            for j in range(len(word)):
                if word[:j+1] == word[:j+1][::-1]:
                    last.append(word[j+1:])
            
            for l in last:
                rl = l[::-1]
                if rl in wordDic:
                    pairs.append([wordDic[rl], i])
                
            # first + last + word
            first = []
            for j in range(len(word)):
                if word[j:] == word[j:][::-1]:
                    first.append(word[:j])
            
            for f in first:
                rf = f[::-1]
                if rf in wordDic:
                    pairs.append([i, wordDic[rf]])
        
        return pairs
