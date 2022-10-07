class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = defaultdict(int)
        i = 0
        for c in order:
            dic[c] = i
            i += 1
            
        for i in range(1, len(words)):
            for j in range(len(words[i-1])):
                if j >= len(words[i]):
                        return False
                if dic[words[i-1][j]] > dic[words[i][j]]:
                    return False
                elif dic[words[i-1][j]] < dic[words[i][j]]:
                    break
        
        return True
