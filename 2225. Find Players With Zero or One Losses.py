class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner = set()
        loser = set()
        oloser = set()

        for m in matches:
            w = m[0]
            l = m[1]

            if w not in loser and w not in oloser and w not in winner:
                winner.add(w)
            
            if l in winner:
                winner.remove(l)
            
            if l not in loser and l not in oloser:
                oloser.add(l)
            elif l not in loser:
                oloser.remove(l)
                loser.add(l)
        
        return [sorted(list(winner)), sorted(list(oloser))]
