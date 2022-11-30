import numpy as np

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = collections.defaultdict(int)

        for n in arr:
            d[n] += 1
        
        o = [n[1] for n in d.items()]
        return len(np.unique(o)) == len(o)
