class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        small = 0
        large = len(tokens) - 1
        score = 0
        
        while small < large:
            if power < tokens[small] and score >= 1:
                power += tokens[large]
                large -= 1
                score -= 1
            elif power >= tokens[small]:
                power -= tokens[small]
                small += 1
                score += 1
            else:
                break
            
        if small == large and power >= tokens[small]:
            score +=1
            
        if score < 0:
            return 0
        
        return score
