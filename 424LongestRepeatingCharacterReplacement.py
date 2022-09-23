from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        long = 0
        scount = Counter()
        left = 0
        
        for i in range(len(s)):
            scount[s[i]] += 1
            
            maxc = scount.most_common(1)[0][1]
            while(sum(scount.values())-maxc > k):
                if scount[s[left]] == 1:
                    scount.pop(s[left])
                else:
                    scount[s[left]] -= 1
                left += 1
                maxc = scount.most_common(1)[0][1]
            
            long = max(long, sum(scount.values()))
        
        return long
